from report.models import ReportResult
import json

from report.report import create_report


def write_report(input_path, output_path: str, file_format: str):
    report = create_report(input_path)
    if file_format == "json":
        with open(output_path, 'w') as outfile:
            json.dump(report.__dict__, outfile)
    elif file_format == "md":
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



write_report("D:/PyPrograms/orders.csv", "report-py-09-062026.md", "md")