"""Exercise custom card inputs through the bundled Easel CLI."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

EXAMPLE = Path(__file__).resolve().parents[1] / "assets/examples/experience-card"
spec = importlib.util.spec_from_file_location("experience_card", EXAMPLE / "reproduce.py")
cards = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cards)


class ExperienceCard(unittest.TestCase):
    def test_custom_quotes_and_separate_dates_survive_revision(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "cards"
            shutil.copytree(EXAMPLE, fixture, ignore=shutil.ignore_patterns("__pycache__"))
            initial = json.loads((fixture / "input-v1.json").read_text())
            initial["quotes"] = ["先打开读者实际点击的链接。"]
            (fixture / "input-v1.json").write_text(json.dumps(initial, ensure_ascii=False))
            provenance = json.loads((fixture / "provenance.json").read_text())
            provenance["revision_date"] = "2026-10-24"
            (fixture / "provenance.json").write_text(json.dumps(provenance))
            with patch.object(cards, "HERE", fixture):
                outputs = cards.replay()
            data = json.loads(outputs["gallery.html"].split('id="card-data">', 1)[1].split("</script>", 1)[0])
            first, revised = data["versions"]
            self.assertEqual([first["day"], revised["day"]], ["2026-10-23", "2026-10-24"])
            self.assertEqual(first["quotes"], initial["quotes"])
            self.assertEqual(revised["quotes"], initial["quotes"])
            self.assertIn(initial["quotes"][0], outputs["card-v2.md"])


if __name__ == "__main__":
    unittest.main()
