import json
from pathlib import Path

import pytest

from report.exceptions import UnsupportedFileFormat
from report.models import ReportResult
from report.writer import write_json, write_markdown, write_report


def test_json_output_exist(
    tmp_path: Path,
    valid_report_results: ReportResult,
    valid_json_report: dict[str, int | float | list[list[str | float]]],
) -> None:
    file_path = tmp_path / "report.json"
    write_json(str(file_path), valid_report_results)
    assert file_path.is_file()


def test_json_output(
    tmp_path: Path,
    valid_report_results: ReportResult,
    valid_json_report: dict[str, int | float | list[list[str | float]]],
) -> None:
    file_path = tmp_path / "report.json"
    write_json(str(file_path), valid_report_results)
    result = json.loads(file_path.read_text(encoding="utf-8"))
    assert result == valid_json_report


def test_md_output_exist(
    tmp_path: Path,
    valid_report_results: ReportResult,
    valid_json_report: dict[str, int | float | list[list[str | float]]],
) -> None:
    file_path = tmp_path / "report.md"
    write_markdown(str(file_path), valid_report_results)
    assert file_path.is_file()


def test_md_output(
    tmp_path: Path, valid_report_results: ReportResult, valid_report_markdown: str
) -> None:
    file_path = tmp_path / "report.md"
    write_markdown(str(file_path), valid_report_results)
    with open(file_path, "r", encoding="utf-8") as file:
        result = file.read()
    assert valid_report_markdown in result


def test_unsupported_file_format(
    tmp_path: Path, valid_report_results: ReportResult, invalid_file_format: str
) -> None:
    file_path = tmp_path / "report.md"
    with pytest.raises(UnsupportedFileFormat):
        write_report(valid_report_results, str(file_path), invalid_file_format)
