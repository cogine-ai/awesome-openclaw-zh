"""Guard the real comedy dialogue against silent gate/SRT parser omissions."""
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "assets/examples/comedy-chase"
spec = importlib.util.spec_from_file_location("comedy_chase", EXAMPLE / "reproduce.py")
comedy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(comedy)


class PinnedDialogueContract:
    """Small compatibility fixture, not a replacement for the actual gate CLI.

    parse_lines uses the fixed 6f16955 gate_check.py's exact dialogue expression;
    the full unmodified tool and timing checks run in reproduce.py.
    """
    @staticmethod
    def parse_units(text):
        return [("fixture feed", text)]

    @staticmethod
    def parse_shots(text):
        return [(int(match[3]), float(match[1]), float(match[2]), line)
                for line in text.splitlines()
                if (match := re.match(r"(\d+)-(\d+)秒 \[镜头(\d+)\]", line))]

    @staticmethod
    def parse_lines(body):
        # MIT-licensed upstream expression; LICENSE.upstream.txt accompanies the pack.
        pattern = r'【([^【】（(:：\n]+?)(?:[（(]([^）)\n]*)[）)])?\s*[:：]\s*["“](.*?)["”]\s*】'
        return [(match[1].strip(), (match[2] or "").strip(), match[3], match[0])
                for match in re.finditer(pattern, body)]


class ComedyChaseDialogue(unittest.TestCase):
    def test_each_original_feed_becomes_one_recognized_dialogue_only_in_the_copy(self):
        for model in ("2.5", "2.0"):
            with self.subTest(model=model):
                path = EXAMPLE / f"seedance-{model}.txt"
                original = path.read_text(encoding="utf-8")
                self.assertEqual(PinnedDialogueContract.parse_lines(original), [])
                adapted, captions = comedy.adapt_gate_copy(original, PinnedDialogueContract)
                self.assertEqual(path.read_text(encoding="utf-8"), original)
                self.assertNotEqual(adapted, original)
                self.assertEqual(len(PinnedDialogueContract.parse_lines(adapted)), 1)
                self.assertEqual(captions, [{"shot": 4, "start": 12, "end": 15, "role": "阿禾",
                                           "tone": "清亮中音、轻快短促、尾音上扬", "text": "连袋也跑？"}])
                self.assertIn('台词：【阿禾（清亮中音、轻快短促、尾音上扬）：“连袋也跑？”】。', adapted)

    def test_silent_gate_parse_cannot_count_as_a_pass(self):
        class SilentParser(PinnedDialogueContract):
            @staticmethod
            def parse_lines(body):
                return []

        original = (EXAMPLE / "seedance-2.5.txt").read_text(encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "did not recognize"):
            comedy.adapt_gate_copy(original, SilentParser)

    def test_changed_dialogue_count_or_unknown_syntax_requires_review(self):
        original = (EXAMPLE / "seedance-2.5.txt").read_text(encoding="utf-8")
        for source in (original.replace("连袋也跑？", ""),
                       original.replace("台词：无。", '台词：{阿禾（轻快）：“帽子呢？”}。', 1)):
            with self.subTest(source=source[-160:]):
                with self.assertRaises(RuntimeError):
                    comedy.adapt_gate_copy(source, PinnedDialogueContract)

    def test_adapter_does_not_invent_tone_or_shorten_overlong_dialogue(self):
        for model in ("2.5", "2.0"):
            with self.subTest(model=model):
                original = (EXAMPLE / f"seedance-{model}.txt").read_text(encoding="utf-8")
                no_tone = original.replace("（清亮中音、轻快短促、尾音上扬）", "")
                checked, captions = comedy.adapt_gate_copy(no_tone, PinnedDialogueContract)
                self.assertEqual(captions[0]["tone"], "")
                self.assertEqual(PinnedDialogueContract.parse_lines(checked)[0][1], "")
                overlong = "跑" * 80 + "？"
                checked, captions = comedy.adapt_gate_copy(
                    original.replace("连袋也跑？", overlong), PinnedDialogueContract)
                self.assertEqual(captions[0]["text"], overlong)
                self.assertEqual(PinnedDialogueContract.parse_lines(checked)[0][2], overlong)

    def test_generated_board_button_exports_real_words_at_12_to_15_seconds(self):
        node = shutil.which("node")
        if node is None:
            self.skipTest("Node.js is required to execute the generated browser SRT function")
        html = (EXAMPLE / "board.html").read_text(encoding="utf-8")
        self.assertEqual(html.count(f"// {comedy.SRT_ADAPTER_MARKER}:"), 1)
        # Execute the actual generated export function with a download capture;
        # no browser downloads or files are created by this test.
        javascript = html[html.index("function fmtSrtTime("):html.index("function exportTimelineCSV(")]
        harness = ("const D={meta:{title:'comedy'}}; let captured;\n"
                   "function dlBlob(name,text,mime){captured={name,text,mime};}\n"
                   + javascript + "\nexportSRT(); process.stdout.write(JSON.stringify(captured));")
        completed = subprocess.run([node, "-e", harness], check=True, capture_output=True,
                                   text=True, encoding="utf-8")
        exported = json.loads(completed.stdout)
        self.assertEqual(exported, {"name": "comedy.srt", "mime": "text/plain;charset=utf-8",
                                    "text": "1\n00:00:12,000 --> 00:00:15,000\n连袋也跑？\n"})
        # The exporter adapter must not rewrite the model text shown in the board.
        data = json.loads(re.search(r"^const D = (.*);$", html, re.M)[1])
        self.assertIn('台词：{阿禾（清亮中音、轻快短促、尾音上扬）：“连袋也跑？”}。',
                      data["segments"][0]["shots"][3]["text"])

    def test_postprocess_refuses_duplicate_or_changed_exporter(self):
        current = (EXAMPLE / "board.html").read_text(encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "Unexpected board exporter"):
            comedy.adapt_board_srt(current, [])
        changed = "function exportSRT(){ changed(); }\nfunction exportTimelineCSV(){ }"
        with self.assertRaisesRegex(RuntimeError, "exporter changed"):
            comedy.adapt_board_srt(changed, [])


if __name__ == "__main__":
    unittest.main()
