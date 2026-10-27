import importlib.util
import json
from pathlib import Path
import subprocess
import unittest

HERE=Path(__file__).resolve().parents[1]/'assets/examples/blind-agent-copy-arena'
spec=importlib.util.spec_from_file_location('copy_arena',HERE/'reproduce.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CopyArena(unittest.TestCase):
    def test_exact_rehearsal_with_explicit_assistant_attribution(self):
        result=module.render(json.loads((HERE/'brief.json').read_text()))
        self.assertEqual(result,(HERE/'index.html').read_text())
        self.assertIn('预置演练',result)
        self.assertIn('不是已执行的 OpenClaw 原生盲测',result)

    def test_invalid_candidate_rejected(self):
        brief=json.loads((HERE/'brief.json').read_text())
        brief['candidates'][0]['text']='过长'*100
        with self.assertRaisesRegex(ValueError,'55'):
            module.render(brief)

    def test_actual_adapter_refuses_unsupported_host_and_preserves_failures(self):
        subprocess.run(['node',str(HERE/'test-native.mjs')],check=True,capture_output=True,timeout=20)


if __name__=='__main__':
    unittest.main()
