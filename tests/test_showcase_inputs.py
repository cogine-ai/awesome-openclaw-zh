"""Prevent a public showcase refresh from publishing private or partial data."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "assets/examples/github-cards"
spec = importlib.util.spec_from_file_location("project_cards", EXAMPLE / "reproduce.py")
cards = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cards)


class PublicShowcaseInputs(unittest.TestCase):
    def setUp(self):
        self.snapshot = json.loads((EXAMPLE / "public-repositories.json").read_text(encoding="utf-8"))

    def assert_refresh_refused_without_overwriting(self, repo):
        response = SimpleNamespace(returncode=0, stdout=json.dumps({"data": {"r0": repo}}))
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "snapshot.json"
            target.write_text("existing public snapshot", encoding="utf-8")
            with patch.object(cards, "SNAPSHOT", target), patch.object(cards.subprocess, "run", return_value=response):
                with self.assertRaises(SystemExit):
                    cards.refresh()
            self.assertEqual(target.read_text(encoding="utf-8"), "existing public snapshot")

    def test_private_or_unexpected_repository_cannot_replace_public_snapshot(self):
        for change in ({"isPrivate": True}, {"nameWithOwner": "another/repository"}):
            with self.subTest(change=change):
                repo = {**self.snapshot["repositories"][0], **change}
                self.assert_refresh_refused_without_overwriting(repo)
                with self.assertRaises(ValueError):
                    cards.data_for_renderers({**self.snapshot, "repositories": [repo]})

    def test_incomplete_language_results_cannot_replace_public_snapshot(self):
        repo = copy.deepcopy(self.snapshot["repositories"][0])
        repo["languages"]["totalCount"] += 1
        self.assert_refresh_refused_without_overwriting(repo)

    def refreshed_response(self):
        repo = copy.deepcopy(self.snapshot["repositories"][0])
        repo["stargazerCount"] += 1
        return SimpleNamespace(returncode=0, stdout=json.dumps({"data": {"r0": repo}}))

    def seed_existing_artifacts(self, directory):
        root = Path(directory)
        for name in ("city.svg", "languages.svg", "rhythm.svg", "index.html", "LICENSE-upstream.txt"):
            (root / name).write_text("existing " + name, encoding="utf-8")
        (root / "public-repositories.json").write_text(
            json.dumps(self.snapshot, ensure_ascii=False), encoding="utf-8",
        )
        return {path.name: path.read_bytes() for path in root.iterdir()}

    def assert_existing_artifacts_unchanged(self, root, before):
        self.assertEqual({path.name: path.read_bytes() for path in root.iterdir()}, before)

    def test_successful_api_read_does_not_publish_snapshot_early(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            before = self.seed_existing_artifacts(root)
            with patch.object(cards, "SNAPSHOT", root / "public-repositories.json"), \
                    patch.object(cards.subprocess, "run", return_value=self.refreshed_response()):
                snapshot = cards.refresh()
            self.assertEqual(snapshot["repositories"][0]["stargazerCount"],
                             self.snapshot["repositories"][0]["stargazerCount"] + 1)
            self.assert_existing_artifacts_unchanged(root, before)

    def test_download_failure_after_api_success_preserves_every_existing_artifact(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            before = self.seed_existing_artifacts(root)
            with patch.object(cards, "ROOT", root), \
                    patch.object(cards, "SNAPSHOT", root / "public-repositories.json"), \
                    patch.object(cards.subprocess, "run", return_value=self.refreshed_response()), \
                    patch.object(cards, "download_renderers", side_effect=OSError("download failed")), \
                    patch.object(cards.sys, "argv", ["reproduce.py", "--refresh"]):
                with self.assertRaisesRegex(OSError, "download failed"):
                    cards.main()
            self.assert_existing_artifacts_unchanged(root, before)

    def test_second_renderer_failure_does_not_publish_the_first_svg_or_snapshot(self):
        first_renderer = SimpleNamespace(render=lambda data: '<svg xmlns="http://www.w3.org/2000/svg"></svg>')

        def fail_render(data):
            raise ValueError("second renderer failed")

        modules = {
            "cards.theme": SimpleNamespace(apply=lambda name: None),
            "cards.card_city": first_renderer,
            "cards.card_languages": SimpleNamespace(render=fail_render),
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            before = self.seed_existing_artifacts(root)
            with patch.object(cards, "ROOT", root), \
                    patch.object(cards, "SNAPSHOT", root / "public-repositories.json"), \
                    patch.object(cards.subprocess, "run", return_value=self.refreshed_response()), \
                    patch.object(cards, "download_renderers"), \
                    patch.object(cards.importlib, "import_module", side_effect=modules.__getitem__), \
                    patch.object(cards.sys, "argv", ["reproduce.py", "--refresh"]):
                with self.assertRaisesRegex(ValueError, "second renderer failed"):
                    cards.main()
            self.assert_existing_artifacts_unchanged(root, before)

    def test_complete_staged_outputs_are_published_before_the_refreshed_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.seed_existing_artifacts(root)
            artifacts = {name: "new " + name for name in
                         ("city.svg", "languages.svg", "rhythm.svg", "index.html", "LICENSE-upstream.txt")}
            refreshed = copy.deepcopy(self.snapshot)
            refreshed["repositories"][0]["stargazerCount"] += 1
            replace = cards.os.replace
            with patch.object(cards, "ROOT", root), \
                    patch.object(cards, "SNAPSHOT", root / "public-repositories.json"), \
                    patch.object(cards.os, "replace", wraps=replace) as replacements:
                cards.publish_artifacts(artifacts, refreshed)
            self.assertEqual(replacements.call_args_list[-1].args[1], root / "public-repositories.json")
            for name, text in artifacts.items():
                self.assertEqual((root / name).read_text(encoding="utf-8"), text)
            self.assertEqual(json.loads((root / "public-repositories.json").read_text(encoding="utf-8")), refreshed)
            self.assertEqual({path.name for path in root.iterdir()}, {*artifacts, "public-repositories.json"})


if __name__ == "__main__":
    unittest.main()
