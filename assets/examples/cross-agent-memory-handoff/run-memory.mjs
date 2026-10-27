#!/usr/bin/env node
// Runnable Sno service source template; not yet validated against a running service.
// No Agent, no source session, no cloud model. Only real passed assertions export a success receipt.
import { spawn } from 'node:child_process';
import { randomBytes } from 'node:crypto';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join, resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { setTimeout as delay } from 'node:timers/promises';

// Fixed Sno 1.6.0 contract-runtime.ts explicitEntry annotates an inspected retired row.
// These checks can be imported for contract tests without starting a service or profile.
export function assertCorrectionHistory(oldEntry, currentEntry, fixture, newId) {
  const expected = `${fixture.original}\nretired; superseded by ${newId}`;
  const metadata = JSON.parse(oldEntry?.metadata ?? '{}');
  if (oldEntry?.text !== expected || currentEntry?.text !== fixture.corrected || metadata.superseded_by !== newId)
    throw new Error('correction did not retain annotated history and matching metadata link');
  return metadata;
}

export async function recallCurrent(client, fixture, scope, oldId, newId) {
  // manual recall deliberately includes retired history in this fixed release.
  const reply = await client.getRecall(fixture.query, scope,
    { source: 'auto', injectionPhase: 'prompt', limit: 5, minScore: 0, maxChars: 2000 });
  if (reply.degraded || !Array.isArray(reply.memoryIds) || !reply.memoryIds.includes(newId)
      || reply.memoryIds.includes(oldId) || !reply.contextText?.includes(fixture.corrected)
      || reply.contextText.includes(fixture.original))
    throw new Error('automatic recall did not select the current text and exclude retired memory');
  return reply;
}

async function main() {
const here = dirname(fileURLToPath(import.meta.url));
const [runtimeArg, profileArg, resultArg] = process.argv.slice(2);
if (!runtimeArg || !profileArg || !resultArg) throw new Error('usage: node run-memory.mjs RUNTIME_PREFIX NEW_PROFILE RESULT_JSON');
const runtime = resolve(runtimeArg), profile = resolve(profileArg), output = resolve(resultArg);
if (existsSync(profile) || existsSync(output)) throw new Error('profile and output must both be new; refusing to overwrite');
if (JSON.parse(readFileSync(join(runtime, 'package.json'), 'utf8')).name !== 'opcboost-public-sno-rehearsal')
  throw new Error('runtime must use this example\'s private package.json in a separate dependency prefix; not a real Sno profile');
const memory = join(runtime, 'node_modules', '@snoai', 'memory');
const version = JSON.parse(readFileSync(join(memory, 'package.json'), 'utf8')).version;
if (version !== '1.6.0') throw new Error('requires @snoai/memory 1.6.0');
const fixture = JSON.parse(readFileSync(join(here, 'fixture.json'), 'utf8'));
const settings = JSON.parse(readFileSync(join(memory, 'settings.default.json'), 'utf8'));
settings.mode = 'local-first';
for (const routes of Object.values(settings.modelCalls)) for (const mode of Object.keys(routes)) routes[mode] = 'off';
settings.user.id = '019a27a0-0000-7000-8000-000000000027';
settings.store = { ...settings.store, path: join(profile, 'memory.sqlite'), encryptionKey: randomBytes(32).toString('hex') };
settings.embedding = { ...settings.embedding, cacheDir: join(runtime, 'models'), threads: 2 };
settings.rerank = { ...settings.rerank, mode: 'none' };
settings.rem = { ...settings.rem, tick: false };
settings.telemetry.observe.enabled = false;
settings.telemetry.memoryUsage.enabled = false;
settings.capture.assistant = false;
settings.capture.ambient = false;
settings.capture.sessionMemory.enabled = false;
settings.logging = { ...settings.logging, level: 'error', file: join(profile, 'runtime.log'), debugContent: false };
settings.memoryPackage = { path: memory, node: process.execPath };
mkdirSync(profile, { recursive: true, mode: 0o700 });
writeFileSync(join(profile, 'settings.json'), JSON.stringify(settings, null, 2) + '\n', { mode: 0o600 });
// Only this process receives the public test profile. HOME and all real Agent config stay unchanged.
process.env.SNO_PROFILE_DIR = profile;
const clientModule = await import(pathToFileURL(join(memory, 'dist', 'client.js')).href);
const server = spawn(process.execPath, [join(memory, 'dist', 'sidecar', 'main.js')], {
  cwd: profile, env: { ...process.env, SNO_PROFILE_DIR: profile }, stdio: ['ignore', 'ignore', 'pipe']
});
let diagnostic = '';
server.stderr.on('data', chunk => { diagnostic = (diagnostic + chunk.toString()).slice(-12000); });
const deadline = Date.now() + 180000;
let ready;
try {
  while (Date.now() < deadline) {
    if (server.exitCode !== null) throw new Error('isolated memory service exited before discovery: ' + diagnostic.slice(-1500));
    if (existsSync(join(profile, 'station', 'sidecar.json'))) { ready = true; break; }
    await delay(200);
  }
  if (!ready) throw new Error('isolated service discovery timed out');
  const clientA = await clientModule.connect({ skinId: 'public-fixture-writer' });
  const clientB = await clientModule.connect({ skinId: 'public-fixture-reader' });
  if (clientA.degraded || clientB.degraded) throw new Error('service connection degraded');
  const scopeA = { principal: clientA.principal, project: fixture.project, session: 'public-writer-session' };
  const scopeB = { principal: clientB.principal, project: fixture.project, session: 'public-reader-session' };
  const ensure = (reply, operation) => {
    if (reply.degraded || reply.result?.isError) throw new Error(operation + ' failed: ' + JSON.stringify(reply));
    return reply;
  };
  ensure(await clientA.init(scopeA, { skinId: 'public-fixture-writer' }), 'writer init');
  ensure(await clientB.init(scopeB, { skinId: 'public-fixture-reader' }), 'reader init');
  console.error('Sno service connected; first store may download the ~639MB local embedding model.');
  const stored = ensure(await clientA.mutate({ op: 'store', content: fixture.original, category: 'episodic' }, scopeA), 'store');
  const oldId = stored.result.details.id;
  if (typeof oldId !== 'string') throw new Error('store returned no memory id');
  const before = ensure(await clientB.inspect({ op: 'get', id: oldId }, scopeB), 'reader get');
  if (before.result.entry?.text !== fixture.original) throw new Error('second client could not read original memory');
  const corrected = ensure(await clientA.mutate({ op: 'correct', id: oldId, content: fixture.corrected }, scopeA), 'correct');
  const newId = corrected.result.details.id;
  if (typeof newId !== 'string' || newId === oldId) throw new Error('correction did not create a successor');
  const old = ensure(await clientB.inspect({ op: 'get', id: oldId }, scopeB), 'get history');
  const current = ensure(await clientB.inspect({ op: 'get', id: newId }, scopeB), 'get successor');
  assertCorrectionHistory(old.result.entry, current.result.entry, fixture, newId);
  await recallCurrent(clientB, fixture, scopeB, oldId, newId);
  const temporary = ensure(await clientA.mutate({ op: 'store', content: fixture.temporary, category: 'episodic' }, scopeA), 'store temporary');
  const temporaryId = temporary.result.details.id;
  if (typeof temporaryId !== 'string') throw new Error('temporary store returned no id');
  ensure(await clientA.mutate({ op: 'forget', id: temporaryId, confirm: true }, scopeA), 'forget temporary');
  const forgotten = ensure(await clientB.inspect({ op: 'get', id: temporaryId }, scopeB), 'get forgotten');
  if (forgotten.result.entry !== null) throw new Error('forgotten entry remains readable');
  const result = {
    status: 'passed',
    testedAt: new Date().toISOString().slice(0, 10), version, sourceCommit: '5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363', nodeVersion: process.version,
    mode: 'local-first', rerank: 'none', llmCallsConfigured: 'off', telemetry: false, realAgentsInvoked: false,
    boundary: 'Real published Sno service + encrypted store + local embeddings; two API clients, not an OpenClaw/Codex handoff.',
    steps: [
      { operation: 'store', client: 'writer', id: 'memory-v1', text: fixture.original, passed: true },
      { operation: 'get', client: 'reader', id: 'memory-v1', text: before.result.entry.text, passed: true },
      { operation: 'correct', client: 'writer', from: 'memory-v1', to: 'memory-v2', text: fixture.corrected, passed: true },
      { operation: 'get-history', client: 'reader', id: 'memory-v1',
        text: old.result.entry.text.slice(0, -newId.length) + 'memory-v2', supersededBy: 'memory-v2',
        normalization: 'Verified runtime successor ID in annotated text and metadata is replaced with alias memory-v2.', passed: true },
      { operation: 'recall-current', client: 'reader', query: fixture.query, source: 'auto', injectionPhase: 'prompt',
        currentText: fixture.corrected, oldTextExcluded: true, passed: true },
      { operation: 'store-and-forget', client: 'writer', text: fixture.temporary, readerGet: null, passed: true }
    ]
  };
  // Deliberately whitelist the public result. No key, token, path, principal or service log is exported.
  writeFileSync(output, JSON.stringify(result, null, 2) + '\n');
  console.log('PASS: real service store/get/correct/history/recall/forget; no real Agent invoked');
} finally {
  server.kill('SIGTERM');
  for (let i = 0; i < 100 && server.exitCode === null; i++) await delay(100);
  if (server.exitCode === null) server.kill('SIGKILL');
}
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) await main();
