import argparse
import logging

from report.exceptions import InvalidCsvError, MissingColumnError
from report.reader import read_file
from report.report import create_report
from report.writer import write_report


def setup_logging() -> None:
    logging.basicConfig(filename='report.log', level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def cli() -> None:
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("CLI started!")
    parser = argparse.ArgumentParser(prog='Brightstone Logistics Report Generator',
                                     description='Convert CSV to JSON or Markdown')
    parser.add_argument('-i', '--input', required=True, type=str,
                        help='Input CSV file path')
    parser.add_argument('-o', '--output', required=True, type=str,
                        help='“Output file path with format (json or markdown)”')
    parser.add_argument('-f', '--format', required=True, type=str,
                        help='Format for output file (json or markdown)',
                        choices=['json', 'markdown'], )
    args = parser.parse_args()

    try:
        orders_list = read_file(args.input)  # -> list[Order]
        report_result = create_report(orders_list)  # -> An instance of the ReportResult class
        write_report(report_result, args.output, args.format)  # -> None (create a file)
    except InvalidCsvError as e:
        logger.error(e)
        print("InvalidCsvError: Invalid CSV format. Please check input file.")
        exit(1)
    except MissingColumnError as e:
        logger.error(e)
        print("MissingColumnError: Column not found. Please check input file.")
        exit(1)
    except OSError as e:
        logger.error(e)
        print("Configuration error: cannot access file system.")
        exit(2)
    except Exception as e:
        logger.error(e)
        print("Unexpected error.")
        exit(2)
    else:
        logger.info("CLI finished successfully!")
        exit(0)
