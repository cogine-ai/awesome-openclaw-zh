"""Exercise failures that could silently break source-to-website publishing."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("catalog", ROOT / "scripts/generate-index.py")
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


class CatalogChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        (self.root / "resources").mkdir()
        (self.root / "usecases/tools").mkdir(parents=True)
        (self.root / "usecases/tools/sample.md").write_text("# Sample\n", encoding="utf-8")
        self.entry = dict(title="Sample", desc="Sample workflow", category="工具开发",
                          localPath="usecases/tools/sample.md", sourceRepo="owner/repo",
                          sourcePath="sample.md", sourceUrl="https://example.com/sample")

    def tearDown(self):
        self.temp.cleanup()

    def load(self, entries):
        (self.root / "resources/usecases-index.json").write_text(json.dumps(entries), encoding="utf-8")
        with patch.object(catalog, "ROOT", self.root):
            return catalog.load_catalog()

    def test_duplicate_and_unindexed_documents_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate path"):
            self.load([self.entry, self.entry])
        (self.root / "usecases/tools/missing-index.md").write_text("# Missing\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "unindexed"):
            self.load([self.entry])

    def test_missing_document_and_wrong_category_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Missing or invalid document"):
            self.load([{**self.entry, "localPath": "usecases/tools/missing.md"}])
        with self.assertRaisesRegex(ValueError, "Wrong category/path"):
            self.load([{**self.entry, "category": "生产力"}])

    def test_malformed_and_non_http_source_links_are_rejected(self):
        for url in ("https:", "https://", "https:///readme.md", "http:broken", "file:///tmp/readme",
                    "https://[broken", "https://example.com:bad", "https://bad host/readme"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                self.load([{**self.entry, "sourceUrl": url}])

    def test_check_detects_drift_without_changing_files(self):
        (self.root / "scripts").mkdir()
        script = self.root / "scripts/generate-index.py"
        script.write_text((ROOT / "scripts/generate-index.py").read_text(encoding="utf-8"), encoding="utf-8")
        self.load([self.entry])
        readme = self.root / "README.md"
        readme.write_text("使用场景：0 个\n", encoding="utf-8")
        (self.root / "resources/usecases-index.md").write_text("stale\n", encoding="utf-8")
        ascii_env = {**os.environ, "LC_ALL": "C", "PYTHONUTF8": "0", "PYTHONCOERCECLOCALE": "0"}
        result = subprocess.run(["python3", str(script), "--check"], capture_output=True, env=ascii_env)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(readme.read_text(encoding="utf-8"), "使用场景：0 个\n")
        subprocess.run(["python3", str(script)], check=True, capture_output=True, env=ascii_env)
        result = subprocess.run(["python3", str(script), "--check"], capture_output=True, env=ascii_env)
        self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
