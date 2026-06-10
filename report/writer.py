import json

from report.models import ReportResult
from report.report import create_report


def write_report(input_path: str, output_path: str, file_format: str) -> None:
    """
    Write report to a file (JSON or Markdown).
    :param input_path: path to input file.
    :param output_path: path to output file.
    :param file_format: format of output file.
    :return: None.
    """
    report = create_report(input_path)
    if file_format == "json":
        write_json(output_path, report)
    elif file_format == "md":
        write_markdown(output_path, report)
    else:
        raise ValueError(f"Unsupported file format: {file_format}")

def write_json(output_path: str, report: ReportResult) -> None:
    """
    Write report to a JSON file.
    :param output_path: path to output file.
    :param report: dataclass ReportResult.
    :return: None.
    """
    with open(output_path, 'w', encoding="utf-8") as outfile:
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

# write_report("D:/PyPrograms/orders.csv", "report.json", "json")