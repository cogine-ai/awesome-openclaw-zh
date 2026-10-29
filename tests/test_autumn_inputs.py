"""Editable example inputs must not escape the chosen output directory."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / 'assets/examples/autumn-makers'
SLUGS = ('sources-to-learning-kit', 'podcast-disagreement-map', 'simulated-product-townhall')


def example(slug):
    path = EXAMPLES / slug
    spec = importlib.util.spec_from_file_location(slug.replace('-', '_'), path / 'reproduce.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    data = json.loads((path / 'input.json').read_text(encoding='utf-8'))
    return module, data


class AutumnInputs(unittest.TestCase):
    def test_current_inputs_rebuild_identical_artifacts(self):
        for slug in SLUGS:
            with self.subTest(slug=slug):
                module, data = example(slug)
                for name, value in module.build(data).items():
                    self.assertEqual((EXAMPLES / slug / name).read_text(encoding='utf-8'), value)

    def test_path_and_selector_ids_are_rejected(self):
        for slug, field in (('sources-to-learning-kit', 'sources'),
                            ('podcast-disagreement-map', 'episodes'),
                            ('simulated-product-townhall', 'roles')):
            module, original = example(slug)
            for invalid in ('../../escape', '/absolute', 'a\\b', 'q\"]:checked', ''):
                with self.subTest(slug=slug, invalid=invalid):
                    data = copy.deepcopy(original)
                    data[field][0]['id'] = invalid
                    with self.assertRaisesRegex(ValueError, 'Invalid .* ID'):
                        module.build(data)

    def test_duplicate_question_ids_and_unsafe_url_segments_are_rejected(self):
        module, data = example('sources-to-learning-kit')
        duplicate = copy.deepcopy(data)
        duplicate['quiz'][1]['id'] = duplicate['quiz'][0]['id']
        with self.assertRaisesRegex(ValueError, 'Duplicate question ID'):
            module.build(duplicate)
        for field in ('category', 'slug'):
            with self.subTest(field=field):
                invalid = copy.deepcopy(data)
                invalid[field] = '\"><img src=x onerror=alert(1)>'
                with self.assertRaisesRegex(ValueError, 'Invalid URL segment'):
                    module.build(invalid)

    def test_all_output_paths_are_checked_before_any_file_is_written(self):
        module, data = example('sources-to-learning-kit')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, output, outside = root / 'input', root / 'output', root / 'outside'
            source.mkdir(); output.mkdir(); outside.mkdir()
            (source / 'input.json').write_text(json.dumps(data), encoding='utf-8')
            (output / 'index.html').write_text('keep existing artifact', encoding='utf-8')
            (output / 'sources').symlink_to(outside, target_is_directory=True)
            with patch.object(module, 'ROOT', source), patch.object(sys, 'argv', ['reproduce.py', '--output-dir', str(output)]):
                with self.assertRaisesRegex(ValueError, 'Symlinked output path'):
                    module.main()
            self.assertEqual((output / 'index.html').read_text(encoding='utf-8'), 'keep existing artifact')
            self.assertFalse((output / 'preview.svg').exists())
            self.assertEqual(list(outside.iterdir()), [])
            with self.assertRaisesRegex(ValueError, 'Invalid output path'):
                module.plan_outputs(output, ['sources/../../escape.md'])

    def test_existing_file_parent_cannot_cause_a_partial_write(self):
        module, data = example('sources-to-learning-kit')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, output = root / 'input', root / 'output'
            source.mkdir(); output.mkdir()
            (source / 'input.json').write_text(json.dumps(data), encoding='utf-8')
            (output / 'index.html').write_text('keep existing artifact', encoding='utf-8')
            (output / 'sources').write_text('keep user file', encoding='utf-8')
            with patch.object(module, 'ROOT', source), patch.object(sys, 'argv', ['reproduce.py', '--output-dir', str(output)]):
                with self.assertRaisesRegex(ValueError, 'Output parent is not a directory'):
                    module.main()
            self.assertEqual((output / 'index.html').read_text(encoding='utf-8'), 'keep existing artifact')
            self.assertFalse((output / 'preview.svg').exists())

    def test_symlinked_output_files_are_rejected(self):
        module, _ = example('sources-to-learning-kit')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / 'original.html'
            target.write_text('keep original', encoding='utf-8')
            (root / 'index.html').symlink_to(target)
            with self.assertRaisesRegex(ValueError, 'Symlinked output path'):
                module.plan_outputs(root, ['index.html'])
            self.assertEqual(target.read_text(encoding='utf-8'), 'keep original')

    def test_validation_still_runs_with_python_optimization(self):
        _, data = example('sources-to-learning-kit')
        data['sources'][0]['id'] = '../../escape'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            script = root / 'reproduce.py'
            script.write_bytes((EXAMPLES / 'sources-to-learning-kit/reproduce.py').read_bytes())
            (root / 'input.json').write_text(json.dumps(data), encoding='utf-8')
            output = root / 'output'
            result = subprocess.run([sys.executable, '-O', str(script), '--output-dir', str(output)],
                                    text=True, capture_output=True, check=False)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Invalid source ID', result.stderr)
            self.assertFalse(output.exists())


if __name__ == '__main__':
    unittest.main()
