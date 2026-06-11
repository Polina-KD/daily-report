import argparse
import logging

from report.exceptions import InvalidCsvError, MissingColumnError, UnsupportedFileFormat
from report.reader import read_file
from report.report import create_report
from report.writer import write_report


def setup_logging() -> None:
    """
    Setup logging

    :return: None
    """
    logging.basicConfig(
        filename="report.log",
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def cli() -> None:
    """
    Main entry point for the Brightstone Logistics CLI tool.

    Parses command-line arguments, runs the full data pipeline,
    and handles errors at the application level.

    The tool:
    - reads a CSV file with orders
    - creates a daily report (totals, top customers/products, revenue per category)
    - saves the report in JSON or Markdown format

    Exit codes:
        0 - success
        1 - input/data error (invalid CSV, missing columns, etc.)
        2 - system error (file access, permissions, unexpected errors)

    :return: None
    """
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("CLI started!")
    parser = argparse.ArgumentParser(
        prog="Brightstone Logistics Report Generator", description="Convert CSV to JSON or Markdown"
    )
    parser.add_argument("-i", "--input", required=True, type=str, help="Input CSV file path")
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=str,
        help="Output file path with format (json or markdown)",
    )
    parser.add_argument(
        "-f", "--format", required=True, type=str, help="Format for output file (json or markdown)"
    )
    args = parser.parse_args()

    try:
        orders_list = read_file(args.input)  # -> list[Order]
        report_result = create_report(orders_list)  # -> An instance of the ReportResult class
        write_report(report_result, args.output, args.format)  # -> None (create a file)
    except UnsupportedFileFormat as e:
        logger.error(e)
        print("UnsupportedFileFormatError: cannot access file system.")
        exit(1)
    except InvalidCsvError as e:
        logger.error(e)
        print("InvalidCsvError: Invalid CSV format. Please check input file.")
        exit(1)
    except MissingColumnError as e:
        logger.error(e)
        print("MissingColumnError: Column not found. Please check input file.")
        exit(1)
    except FileNotFoundError as e:
        logger.error(e)
        print("FileNotFoundError: cannot find the file.")
        exit(2)
    except PermissionError as e:
        logger.error(e)
        print("PermissionError: Permission denied.")
        exit(2)
    except Exception as e:
        logger.error(e)
        print("Unexpected error.")
        exit(2)
    else:
        logger.info("CLI finished successfully!")
        exit(0)
