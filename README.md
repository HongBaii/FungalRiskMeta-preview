# FungalRiskMeta

FungalRiskMeta is a Python command-line framework for fungal metagenomic risk assessment. This public repository provides a lightweight project preview while the complete research implementation is maintained privately during manuscript preparation.

Research resources, full workflows, datasets, and manuscript materials are not included in this public preview.

## Current Scope

The public preview includes:

- Python package and CLI skeleton.
- Minimal toy example files.
- A lightweight smoke test for the public preview CLI.
- High-level public-preview documentation.

The public preview does not include:

- Research resources.
- Full analysis workflows.
- Validation outputs.
- Unpublished study materials.

## Installation

```bash
conda env create -f environment.yml
conda activate fungalriskmeta-preview
pip install -e .
```

The package installs two CLI aliases:

```bash
fungalriskmeta --help
```

## Minimal Demo

The minimal example runs a public-preview command on toy TSV files and writes a small placeholder report. This command is intended to demonstrate installation, CLI structure, and file handling only.

```bash
python -m fungalriskmeta demo \
  --input-table examples/minimal/input_table.tsv \
  --metadata examples/minimal/metadata.tsv \
  --sample demo \
  --outdir examples/minimal/preview_out
```

Expected output:

- `examples/minimal/preview_out/preview_report.tsv`

Bundled toy inputs:

- `examples/minimal/input_table.tsv`
- `examples/minimal/metadata.tsv`

## Tests

```bash
python -m unittest tests.test_public_preview
```

## Development Status

FungalRiskMeta is under active development. This public preview is intended to document the project structure and provide a stable placeholder for collaborators, readers, and future releases.

## Citation

Citation information will be added after manuscript deposition.
