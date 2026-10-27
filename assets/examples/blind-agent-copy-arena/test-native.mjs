// Contract regression with a fake host; this is NOT live OpenClaw execution.
import assert from 'node:assert/strict';
import {runBlindTrial} from './native-trial.mjs';
let calls=0;
await assert.rejects(runBlindTrial({runtime:{capabilities:[]}},'task','r1'),/unavailable/);
assert.equal(calls,0);
const api={runtime:{capabilities:['native-subagent-blind-v1'],subagent:{native:{
 async spawn(args){calls++;assert.equal(args.context,'isolated');assert.equal(args.blind,true);assert.equal('model' in args,false);return {runId:'fixture-only',selection:{requested:{}}};},
 async collect(args){assert.deepEqual(args,{ids:['fixture-only'],awaitResults:true});return {results:[{status:'failed',error:'fixture failure'}]};}
}}}};
const receipts=await runBlindTrial(api,'reviewed brief','r1');
assert.equal(calls,1);
assert.equal(receipts.collected.results[0].status,'failed');
await assert.rejects(runBlindTrial(api,'','r2'),/required/);
assert.equal(calls,1);
console.log('Native adapter contract regression passed with fake host; live trial not executed.');
