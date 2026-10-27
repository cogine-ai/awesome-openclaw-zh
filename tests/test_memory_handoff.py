"""Integrity checks for an honest experimental Sno delivery, with no service/Agent run."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "assets/examples/cross-agent-memory-handoff"
SPEC = importlib.util.spec_from_file_location("memory_handoff", SOURCE / "reproduce.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class MemoryHandoffTest(unittest.TestCase):
    def run_script(self, root, *arguments):
        return subprocess.run([sys.executable, str(root / "reproduce.py"), *arguments], capture_output=True, text=True)

    def test_blocked_offline_replay_stays_unverified(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "copy"
            result = self.run_script(SOURCE, "--out", str(out))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("memory operations remain UNVERIFIED", result.stdout)
            replay = self.run_script(out, "--verify")
            self.assertEqual(replay.returncode, 0, replay.stderr)
            self.assertEqual((out / "preview.svg").read_bytes(), (SOURCE / "preview.svg").read_bytes())
            self.assertIn("不是成功演示", (out / "index.html").read_text())

    def test_tampered_input_fails_before_output(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "fixture"
            shutil.copytree(SOURCE, fixture)
            card = fixture / "fixture.json"
            value = json.loads(card.read_text())
            value["corrected"] = "A different private input"
            card.write_text(json.dumps(value))
            out = Path(directory) / "not-created"
            result = self.run_script(fixture, "--out", str(out))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("public input differs", result.stderr)
            self.assertFalse(out.exists())

    def test_blocked_receipt_cannot_claim_agent_success(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "fixture"
            shutil.copytree(SOURCE, fixture)
            receipt = fixture / "receipt.json"
            value = json.loads(receipt.read_text())
            value["realAgentsInvoked"] = True
            receipt.write_text(json.dumps(value))
            result = self.run_script(fixture, "--verify")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("recording boundary changed", result.stderr)

    def test_record_needs_a_real_run_and_existing_out_is_preserved(self):
        result = self.run_script(SOURCE, "--record")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cannot manufacture", result.stderr)
        with tempfile.TemporaryDirectory() as directory:
            marker = Path(directory) / "preserve.txt"
            marker.write_text("unrelated work")
            result = self.run_script(SOURCE, "--out", directory)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(marker.read_text(), "unrelated work")

    def test_sno_contract_checks_annotated_history_and_auto_recall(self):
        # Fixed-contract synthetic replies only: no Sno dependency, service or Agent.
        code = '''
import assert from 'node:assert/strict';
import {assertCorrectionHistory, recallCurrent} from MODULE;
const fixture={original:'public old fact',corrected:'public new fact',query:'public query'};
const current={text:fixture.corrected,metadata:'{}'};
const old={text:fixture.original+'\\nretired; superseded by runtime-new',metadata:JSON.stringify({superseded_by:'runtime-new'})};
assert.equal(assertCorrectionHistory(old,current,fixture,'runtime-new').superseded_by,'runtime-new');
assert.throws(()=>assertCorrectionHistory({...old,text:fixture.original},current,fixture,'runtime-new'),/annotated history/);
assert.throws(()=>assertCorrectionHistory({...old,metadata:JSON.stringify({superseded_by:'wrong'})},current,fixture,'runtime-new'),/metadata link/);
const scope={project:'public-fixture'};
let calls=0;
const client={async getRecall(query,actualScope,options){
 calls++;assert.equal(query,fixture.query);assert.equal(actualScope,scope);
 assert.deepEqual(options,{source:'auto',injectionPhase:'prompt',limit:5,minScore:0,maxChars:2000});
 return {degraded:false,contextText:fixture.corrected,memoryIds:['runtime-new']};
}};
await recallCurrent(client,fixture,scope,'runtime-old','runtime-new');assert.equal(calls,1);
await assert.rejects(recallCurrent({async getRecall(){return {degraded:false,contextText:old.text+' '+fixture.corrected,memoryIds:['runtime-old','runtime-new']};}},fixture,scope,'runtime-old','runtime-new'),/exclude retired/);
await assert.rejects(recallCurrent({async getRecall(){return {degraded:false,contextText:fixture.corrected,memoryIds:['runtime-old']};}},fixture,scope,'runtime-old','runtime-new'),/exclude retired/);
'''.replace("MODULE", json.dumps((SOURCE / "run-memory.mjs").as_uri()))
        subprocess.run(["node", "--input-type=module", "-e", code], check=True, capture_output=True, text=True, timeout=20)

    def test_receipt_validator_enforces_history_annotation_and_auto_source(self):
        # This success-shaped object is an in-memory validation fixture, never a run receipt.
        fixture = json.loads((SOURCE / "fixture.json").read_text())
        receipt = json.loads((SOURCE / "receipt.json").read_text())
        receipt.update(status="passed", steps=[
            {"operation":"store","text":fixture["original"],"passed":True},
            {"operation":"get","text":fixture["original"],"passed":True},
            {"operation":"correct","text":fixture["corrected"],"passed":True},
            {"operation":"get-history","text":fixture["original"]+"\nretired; superseded by memory-v2","supersededBy":"memory-v2","normalization":"Verified runtime successor ID in annotated text and metadata is replaced with alias memory-v2.","passed":True},
            {"operation":"recall-current","currentText":fixture["corrected"],"oldTextExcluded":True,"source":"auto","injectionPhase":"prompt","passed":True},
            {"operation":"store-and-forget","readerGet":None,"passed":True},
        ])
        MODULE.validate(receipt)
        bad = copy.deepcopy(receipt)
        bad["steps"][3]["text"] = fixture["original"]
        with self.assertRaisesRegex(ValueError, "correction history"):
            MODULE.validate(bad)
        bad = copy.deepcopy(receipt)
        bad["steps"][4]["source"] = "manual"
        with self.assertRaisesRegex(ValueError, "current-only recall"):
            MODULE.validate(bad)


if __name__ == "__main__":
    unittest.main()
