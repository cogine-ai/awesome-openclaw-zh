"""Public bundles must exclude unrelated files and reject unsafe manifest paths."""
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location('autumn_bundles', Path(__file__).resolve().parents[1] / 'assets/examples/autumn-makers/build-bundles.py')
bundles = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bundles)


class AutumnBundles(unittest.TestCase):
    def test_explicit_manifest_excludes_unlisted_private_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'case.md').write_text('Public example')
            (root / 'private.json').write_text('private secret')
            pack = {'title': 'Example', 'case': 'case.md', 'files': ['case.md']}
            first = bundles.bundle_bytes(root, pack)
            self.assertEqual(first, bundles.bundle_bytes(root, pack))
            with zipfile.ZipFile(io.BytesIO(first)) as archive:
                self.assertIsNone(archive.testzip())
                self.assertEqual(set(archive.namelist()), {'case.md', 'START-HERE.md', 'BUNDLE-SOURCE.json'})
                self.assertNotIn(b'private secret', b''.join(archive.read(name) for name in archive.namelist()))

    def test_traversal_and_symlink_cannot_enter_bundle(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'public.txt').write_text('public')
            (root / 'linked.txt').symlink_to(root / 'public.txt')
            for relative in ['../outside.txt', '/etc/passwd', 'a/../public.txt', 'a\\public.txt', 'linked.txt']:
                with self.subTest(relative=relative), self.assertRaises(ValueError):
                    bundles.read_public_file(root, relative)
