"""Integrity checks for an honest experimental Sno delivery, with no service/Agent run."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "assets/examples/cross-agent-memory-handoff"


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


if __name__ == "__main__":
    unittest.main()
