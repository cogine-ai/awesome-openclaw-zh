"""Protect offline/paid-service boundaries while replaying the real pinned planner."""
import importlib.util
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parents[1] / "assets/examples/digital-human-product-intro"
spec = importlib.util.spec_from_file_location("digital_intro", HERE / "reproduce.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class OfflineIntro(unittest.TestCase):
    def setUp(self):
        self.script = json.loads((HERE / "script.json").read_text())
        self.persona = json.loads((HERE / "persona.offline.json").read_text())

    def test_replay_is_exact_and_cannot_claim_media_or_price(self):
        plan = module.planned_tasks(self.script, self.persona)
        self.assertFalse(plan["readyToSubmit"])
        self.assertFalse(plan["generatedVideo"])
        self.assertIsNone(plan["estimatedCredits"])
        self.assertEqual(plan["priceStatus"], "not-quoted")
        self.assertEqual(sum(task["duration"] for task in plan["tasks"]), 26)
        for name, content in module.outputs(plan, self.script).items():
            self.assertEqual(content, (HERE / name).read_text())

    def test_upstream_rejects_overlong_narration(self):
        self.script[0]["t"] = "这是一段很长的口播。" * 30
        with self.assertRaisesRegex(ValueError, "超过"):
            module.planned_tasks(self.script, self.persona)

    def test_duplicate_segments_are_rejected(self):
        self.script[1]["id"] = self.script[0]["id"]
        with self.assertRaisesRegex(ValueError, "duplicate"):
            module.planned_tasks(self.script, self.persona)


if __name__ == "__main__":
    unittest.main()
