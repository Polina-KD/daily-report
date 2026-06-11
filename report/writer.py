import json
import logging

from report.exceptions import UnsupportedFileFormat
from report.models import ReportResult

logger = logging.getLogger(__name__)


def write_report(report: ReportResult, output_path: str, file_format: str) -> None:
    """
    Write report to a file (JSON or Markdown).
    :param report: an instance of the ReportResult dataclass.
    :param output_path: path to output file.
    :param file_format: format of output file.
    :return: None.
    """
    if file_format == "json":
        write_json(output_path, report)
        logger.info(f"Report written to {output_path} in JSON format.")
    elif file_format == "markdown":
        write_markdown(output_path, report)
        logger.info(f"Report written to {output_path} in Markdown format.")
    else:
        raise UnsupportedFileFormat(f"Unsupported file format: {file_format}")


def write_json(output_path: str, report: ReportResult) -> None:
    """
    Write report to a JSON file.
    :param output_path: path to output file.
    :param report: dataclass ReportResult.
    :return: None.
    """
    with open(output_path, "w", encoding="utf-8") as outfile:
        json.dump(report.__dict__, outfile, indent=4)


def write_markdown(output_path: str, report: ReportResult) -> None:
    """
    Write report to a Markdown file.
    :param output_path: path to output file.
    :param report: dataclass ReportResult.
    :return: None.
    """
    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write("# Daily Report\n\n")

        outfile.write("## Summary\n\n")
        outfile.write(f"- Total orders: {report.total_orders}\n")
        outfile.write(f"- Total revenue: {report.total_revenue}\n\n")

        outfile.write("## Top products\n")
        for name, value in report.top_products:
            outfile.write(f"- {name} — {value}\n")

        outfile.write("\n## Top customers\n")
        for name, value in report.top_customers:
            outfile.write(f"- {name} — {value}\n")

        outfile.write("\n## Revenue per category\n")
        for name, value in report.revenue_by_category:
            outfile.write(f"- {name} — {value}\n")


# write_report("D:/PyPrograms/order.csv", "report.json", "json")
