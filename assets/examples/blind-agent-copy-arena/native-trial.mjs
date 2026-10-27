/** Adapter for an eligible OpenClaw reply_dispatch handler, NOT an installable plugin.
 * Contract pinned to openclaw/openclaw@43dc38e6c1370e7682156b8a84ed6fc1abfaa0b7.
 * No process launch, credential read, or network call on import.
 */
export async function runBlindTrial(api, task, requestId) {
  if (!Array.isArray(api?.runtime?.capabilities) || !api.runtime.capabilities.includes('native-subagent-blind-v1')) {
    throw new Error('Native blinding unavailable; no trial launched');
  }
  const native = api.runtime.subagent?.native;
  if (!native?.spawn || !native?.collect) throw new Error('Requester-bound native runtime unavailable');
  if (typeof task !== 'string' || !task.trim() || typeof requestId !== 'string' || !requestId.trim()) {
    throw new Error('A reviewed task and stable requestId are required');
  }
  // The host supplies requester authority; callers cannot manufacture it from a JSON file.
  // Keep model selection at its configured default; use host-authorized overrides separately.
  const accepted = await native.spawn({requestId, task, context:'isolated', blind:true});
  if (!accepted?.runId) throw new Error('Missing native acceptance receipt');
  const collected = await native.collect({ids:[accepted.runId], awaitResults:true});
  return {accepted, collected}; // Retain real receipts/status; an accepted request is not a completed answer.
}
