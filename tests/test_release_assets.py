"""Keep unreviewed local inputs out of release attachments."""
from contextlib import redirect_stdout
import importlib.util
import io
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location(
    "release_assets", Path(__file__).resolve().parents[1] / "releases/prepare-assets.py",
)
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReviewedReleaseAssets(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="showcase-release-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "source"
        self.root.mkdir()
        self.output = Path(self.temporary.name) / "release"
        files = {"LICENSE", *release.PACKS.values()}
        for name, assets in release.PACK_ASSETS.items():
            files.update(f"assets/examples/{name}/{asset}" for asset in assets)
        for relative in files:
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(f"Reviewed public content: {relative}\n", encoding="utf-8")
        self.git("init", "--quiet", "--template=")
        self.git("add", ".")
        self.git("-c", "core.hooksPath=/dev/null", "-c", "commit.gpgsign=false",
                 "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "commit", "--quiet", "-m", "Reviewed fixture")

    def git(self, *arguments):
        subprocess.run(["git", *arguments], cwd=self.root, check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def test_untracked_private_inputs_are_never_included(self):
        private = self.root / "assets/examples/experience-card/private-interview.json"
        private.write_text('{"private":"do not publish"}', encoding="utf-8")
        with redirect_stdout(io.StringIO()):
            release.prepare_assets(self.root, self.output)
        archives = list(self.output.glob("*.zip"))
        self.assertEqual(len(archives), 3)
        for path in archives:
            with zipfile.ZipFile(path) as archive:
                self.assertIsNone(archive.testzip())
                self.assertNotIn(private.relative_to(self.root).as_posix(), archive.namelist())
                self.assertFalse(any(b"do not publish" in archive.read(name) for name in archive.namelist()))
                self.assertIn("LICENSE", archive.namelist())
                self.assertIn("START-HERE.md", archive.namelist())

    def test_changed_reviewed_input_is_refused_before_any_archive_is_created(self):
        source = self.root / "assets/examples/experience-card/input-v1.json"
        source.write_text('{"private":"new local interview"}', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "tracked and unchanged"):
            release.prepare_assets(self.root, self.output)
        self.assertFalse(self.output.exists())

    def test_symlinked_input_is_refused_before_any_archive_is_created(self):
        source = self.root / "assets/examples/experience-card/input-v1.json"
        private = Path(self.temporary.name) / "private.json"
        private.write_text("private", encoding="utf-8")
        source.unlink()
        source.symlink_to(private)
        with self.assertRaisesRegex(ValueError, "symlinked"):
            release.prepare_assets(self.root, self.output)
        self.assertFalse(self.output.exists())


if __name__ == "__main__":
    unittest.main()
