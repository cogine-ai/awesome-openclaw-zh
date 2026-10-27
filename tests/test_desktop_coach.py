"""Regression checks for the public, offline desktop-coach delivery."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[1] / "assets/examples/interactive-desktop-coach"
SPEC = importlib.util.spec_from_file_location("desktop_coach", SOURCE / "reproduce.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class DesktopCoachTest(unittest.TestCase):
    def run_script(self, root, *arguments):
        return subprocess.run([sys.executable, str(root / "reproduce.py"), *arguments], capture_output=True, text=True)

    def test_offline_replay_and_new_copy(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "copy"
            result = self.run_script(SOURCE, "--out", str(out))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((out / "index.html").read_bytes(), (SOURCE / "index.html").read_bytes())
            replay = self.run_script(out, "--verify")
            self.assertEqual(replay.returncode, 0, replay.stderr)
            self.assertIn("CLI was not rerun", replay.stdout)

    def test_input_tamper_fails_before_creating_output(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "fixture"
            shutil.copytree(SOURCE, fixture)
            card = fixture / "cards/01-open.json"
            data = json.loads(card.read_text())
            data["title"] = "Changed after CLI validation"
            card.write_text(json.dumps(data))
            out = Path(directory) / "must-not-exist"
            result = self.run_script(fixture, "--out", str(out))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("differs from real CLI recording", result.stderr)
            self.assertFalse(out.exists())

    def test_existing_output_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory)
            marker = out / "preserve.txt"
            marker.write_text("unrelated work")
            result = self.run_script(SOURCE, "--out", str(out))
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(marker.read_text(), "unrelated work")
            self.assertFalse((out / "index.html").exists())

    def test_desktop_is_explicit_and_requires_cli(self):
        result = self.run_script(SOURCE, "--desktop")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("require an explicit --cli", result.stderr)

    def test_version_probe_is_bounded_before_any_card(self):
        # Contract-only timeout fixture; it does not run the upstream CLI.
        with patch.object(MODULE.subprocess, "run", side_effect=subprocess.TimeoutExpired(["fixture-binary", "--version"], 20)) as run:
            with self.assertRaises(subprocess.TimeoutExpired):
                MODULE.run_cli(Path("fixture-binary"))
        self.assertEqual(run.call_count, 1)
        self.assertEqual(run.call_args.args[0], ["fixture-binary", "--version"])
        self.assertEqual(run.call_args.kwargs["timeout"], 20)


if __name__ == "__main__":
    unittest.main()
