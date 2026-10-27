"""Protect offline/paid-service boundaries while replaying the real pinned planner."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parents[1] / "assets/examples/digital-human-product-intro"
spec = importlib.util.spec_from_file_location("digital_intro", HERE / "reproduce.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class OfflineIntro(unittest.TestCase):
    def setUp(self):
        self.script = json.loads((HERE / "script.json").read_text(encoding="utf-8"))
        self.persona = json.loads((HERE / "persona.offline.json").read_text(encoding="utf-8"))

    def test_replay_is_exact_and_cannot_claim_media_or_price(self):
        plan = module.planned_tasks(self.script, self.persona)
        self.assertFalse(plan["readyToSubmit"])
        self.assertFalse(plan["generatedVideo"])
        self.assertIsNone(plan["estimatedCredits"])
        self.assertEqual(plan["priceStatus"], "not-quoted")
        self.assertEqual(sum(task["duration"] for task in plan["tasks"]), 26)
        for name, content in module.outputs(plan, self.script).items():
            self.assertEqual(content, (HERE / name).read_text(encoding="utf-8"))

    def test_upstream_rejects_overlong_narration(self):
        self.script[0]["t"] = "这是一段很长的口播。" * 30
        with self.assertRaisesRegex(ValueError, "超过"):
            module.planned_tasks(self.script, self.persona)

    def test_duplicate_segments_are_rejected(self):
        self.script[1]["id"] = self.script[0]["id"]
        with self.assertRaisesRegex(ValueError, "duplicate"):
            module.planned_tasks(self.script, self.persona)

    def test_blank_narration_lines_do_not_split_the_srt_cue(self):
        original = "第一句。\n\n第二句。"
        self.script[0]["t"] = original
        plan = module.planned_tasks(self.script, self.persona)
        subtitles = module.outputs(plan, self.script)["planned-subtitles.srt"]
        self.assertTrue(subtitles.split("\n\n")[0].endswith("第一句。 第二句。"))
        self.assertEqual(self.script[0]["t"], original)

    def test_replay_does_not_depend_on_the_parent_default_text_encoding(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "intro"
            env = {**os.environ, "LC_ALL": "C", "PYTHONUTF8": "0", "PYTHONCOERCECLOCALE": "0"}
            subprocess.run([sys.executable, "-X", "utf8=0", str(HERE / "reproduce.py"),
                            "--output-dir", str(output)], env=env,
                           check=True, capture_output=True, timeout=20)
            self.assertIn("先把口播分好段", (output / "index.html").read_text(encoding="utf-8"))
            self.assertEqual((output / "planned-subtitles.srt").read_bytes(), (HERE / "planned-subtitles.srt").read_bytes())


if __name__ == "__main__":
    unittest.main()
