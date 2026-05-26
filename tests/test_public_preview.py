from __future__ import annotations

import unittest
import tempfile
from pathlib import Path

from fungalriskmeta.cli import main


class PublicPreviewTests(unittest.TestCase):
    def test_cli_help_exits_cleanly(self) -> None:
        with self.assertRaises(SystemExit) as exc:
            main(["--help"])
        self.assertEqual(exc.exception.code, 0)

    def test_demo_command_exits_cleanly(self) -> None:
        self.assertEqual(main(["demo"]), 0)

    def test_demo_writes_preview_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            outdir = Path(tmp) / "out"
            self.assertEqual(main(["demo", "--outdir", str(outdir), "--sample", "S1"]), 0)
            report = outdir / "preview_report.tsv"
            self.assertTrue(report.exists())
            text = report.read_text(encoding="utf-8")
            self.assertIn("S1", text)
            self.assertIn("preview_complete", text)


if __name__ == "__main__":
    unittest.main()
