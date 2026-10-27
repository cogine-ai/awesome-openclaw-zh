"""Validate the decision boundary without downloading a model in ordinary CI."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import subprocess
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch
from contextlib import nullcontext

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "assets/examples/local-decision-snake"
spec = importlib.util.spec_from_file_location("local_snake", EXAMPLE / "reproduce.py")
snake = importlib.util.module_from_spec(spec)
spec.loader.exec_module(snake)


class LocalSnake(unittest.TestCase):
    def setUp(self):
        self.scenario = json.loads((EXAMPLE / "scenario.json").read_text(encoding="utf-8"))

    def test_standalone_export_retains_trace_replay_and_return_links(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "snake"
            subprocess.run([sys.executable, str(EXAMPLE / "reproduce.py"), "--output-dir", str(output)],
                           check=True, capture_output=True, timeout=20)
            subprocess.run([sys.executable, str(output / "reproduce.py")],
                           check=True, capture_output=True, timeout=20)
            for name in ("run.json", "scenario.json", "LICENSE.laya.txt", "LICENSE.snake-reference.txt"):
                self.assertTrue((output / name).is_file())
            self.assertIn("/usecases/creative/local-decision-snake-lab/", (output / "index.html").read_text())

    def test_baseline_is_deterministic_and_has_no_fake_model_statistics(self):
        first, second = snake.play(self.scenario), snake.play(self.scenario)
        self.assertEqual(first, second)
        self.assertEqual(first["mode"], "planner-baseline")
        self.assertTrue(first["frames"])
        for frame in first["frames"]:
            self.assertIsNone(frame["probabilities"])
            self.assertIsNone(frame["latencyMs"])

    def test_guard_changes_an_unsafe_proposal_without_hiding_it(self):
        scenario = {"width": 4, "height": 4, "seed": 7, "steps": 1}
        # DOWN hits the wall in the actual initial 4x4 state.
        def wrong_model(state, questions):
            return {"answers": {"move": {"probabilities": {"UP": .2, "DOWN": .7, "LEFT": .05, "RIGHT": .05}}}}
        run = snake.play(scenario, wrong_model)
        self.assertEqual(run["frames"][0]["proposed"], "DOWN")
        self.assertNotEqual(run["frames"][0]["executed"], "DOWN")
        self.assertTrue(run["frames"][0]["shield"])
        self.assertEqual(run["shieldInterventions"], 1)

    def test_invalid_model_distributions_are_errors_not_planner_fallbacks(self):
        for probabilities in ({"UP": 1}, {name: float("nan") for name in snake.DIRS},
                              {name: .7 for name in snake.DIRS}):
            with self.subTest(probabilities=probabilities):
                with self.assertRaises(ValueError):
                    snake.check_probabilities(probabilities)

    def test_wrong_or_partial_weights_are_refused_before_importing_a_model(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            (path / "model.safetensors").write_bytes(b"partial")
            with self.assertRaisesRegex(ValueError, "842,609,210"):
                snake.verify_weights(path)

    def test_short_range_never_becomes_a_completed_checkpoint(self):
        response = SimpleNamespace(status=206, headers={"Content-Range": "bytes 0-7/8"}, read=lambda limit: b"123")
        with tempfile.TemporaryDirectory() as directory, \
             patch.object(snake, "MODEL_FILES", ("model.safetensors",)), \
             patch.object(snake, "WEIGHT_BYTES", 8), \
             patch.object(snake.urllib.request, "urlopen", return_value=nullcontext(response)):
            with self.assertRaisesRegex(ValueError, "Short checkpoint range"):
                snake.download_model(Path(directory))
            self.assertFalse((Path(directory) / "model.safetensors").exists())

    def test_explicit_retry_resumes_prefix_and_checks_full_hash(self):
        response = SimpleNamespace(status=206, headers={"Content-Range": "bytes 3-7/8"}, read=lambda limit: b"45678")
        with tempfile.TemporaryDirectory() as directory, \
             patch.object(snake, "MODEL_FILES", ("model.safetensors",)), \
             patch.object(snake, "WEIGHT_BYTES", 8), \
             patch.object(snake, "WEIGHT_SHA256", hashlib.sha256(b"12345678").hexdigest()), \
             patch.object(snake.urllib.request, "urlopen", return_value=nullcontext(response)) as fetch:
            root = Path(directory)
            (root / "model.safetensors.part").write_bytes(b"123")
            snake.download_model(root)
            self.assertEqual(fetch.call_args.args[0].get_header("Range"), "bytes=3-7")
            self.assertEqual((root / "model.safetensors").read_bytes(), b"12345678")
            self.assertFalse((root / "model.safetensors.part").exists())

    def test_recorded_replay_rejects_unsafe_or_fabricated_moves(self):
        path = EXAMPLE / "run.json"
        trace = json.loads(path.read_text(encoding="utf-8"))
        snake.validate_trace(trace)
        self.assertEqual(trace["mcp"]["modelInferenceThroughMcp"], False)
        self.assertEqual(trace["mcp"]["openclawEndToEnd"], False)
        changed = copy.deepcopy(trace)
        changed["runs"][0]["frames"][0]["snake"][0] = [999, 999]
        with self.assertRaisesRegex(ValueError, "Falsified"):
            snake.validate_trace(changed)
        changed = copy.deepcopy(trace)
        changed["runs"][0]["score"] += 10
        with self.assertRaisesRegex(ValueError, "Run summary"):
            snake.validate_trace(changed)


if __name__ == "__main__":
    unittest.main()
