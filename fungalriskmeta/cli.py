from __future__ import annotations

import argparse
import csv
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="fungalriskmeta",
        description=(
            "Public preview CLI for FungalRiskMeta. Full analysis modules, "
            "resources, and workflows are maintained separately during "
            "manuscript preparation."
        ),
    )
    parser.add_argument(
        "--version",
        action="version",
        version="FungalRiskMeta public preview 0.0.1",
    )

    subparsers = parser.add_subparsers(dest="command")
    demo = subparsers.add_parser("demo", help="Run the bundled public-preview demo.")
    demo.add_argument(
        "--root",
        default="examples/minimal",
        help="Path to the minimal example directory.",
    )
    demo.add_argument(
        "--input-table",
        default=None,
        help="Toy input table for the public-preview demo.",
    )
    demo.add_argument(
        "--metadata",
        default=None,
        help="Toy metadata table for the public-preview demo.",
    )
    demo.add_argument(
        "--sample",
        default="demo",
        help="Sample identifier for the public-preview demo.",
    )
    demo.add_argument(
        "--outdir",
        default="examples/minimal/preview_out",
        help="Output directory for the public-preview demo.",
    )
    return parser


def _count_data_rows(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle, delimiter="\t")
        next(reader, None)
        return sum(1 for row in reader if row)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "demo":
        root = Path(args.root)
        input_table = Path(args.input_table) if args.input_table else root / "input_table.tsv"
        metadata = Path(args.metadata) if args.metadata else root / "metadata.tsv"
        outdir = Path(args.outdir)
        outdir.mkdir(parents=True, exist_ok=True)
        report = outdir / "preview_report.tsv"

        input_rows = _count_data_rows(input_table)
        metadata_rows = _count_data_rows(metadata)
        with report.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["sample", "input_rows", "metadata_rows", "status", "note"],
                delimiter="\t",
                lineterminator="\n",
            )
            writer.writeheader()
            writer.writerow(
                {
                    "sample": args.sample,
                    "input_rows": input_rows,
                    "metadata_rows": metadata_rows,
                    "status": "preview_complete",
                    "note": "public_preview_only",
                }
            )

        print("FungalRiskMeta public preview")
        print(f"Input table: {input_table}")
        print(f"Metadata table: {metadata}")
        print(f"Output report: {report}")
        return 0

    parser.print_help()
    return 0
