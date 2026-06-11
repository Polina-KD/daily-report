from pathlib import Path

import pytest
from _pytest.monkeypatch import MonkeyPatch

from report.cli import cli


def test_successful_path(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    output_file = tmp_path / "output.json"

    monkeypatch.setattr(
        "sys.argv",
        [
            "report",
            "--input",
            "tests/data/valid_orders.csv",
            "--output",
            str(output_file),
            "--format",
            "json",
        ],
    )

    with pytest.raises(SystemExit) as e:
        cli()
    assert e.value.code == 0


def test_exit_1_path(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    output_file = tmp_path / "output.json"
    invalid_input_file = "tests/data/invalid_orders.csv"

    monkeypatch.setattr(
        "sys.argv",
        [
            "report",
            "--input",
            invalid_input_file,
            "--output",
            str(output_file),
            "--format",
            "json",
        ],
    )

    with pytest.raises(SystemExit) as e:
        cli()
    assert e.value.code == 1


def test_exit_2_path(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    output_file = tmp_path / "output.json"
    invalid_input_file = "tests/data/valid_orders"

    monkeypatch.setattr(
        "sys.argv",
        [
            "report",
            "--input",
            invalid_input_file,
            "--output",
            str(output_file),
            "--format",
            "json",
        ],
    )

    with pytest.raises(SystemExit) as e:
        cli()
    assert e.value.code == 2
