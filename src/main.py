import logging
import sys
from parameters import run_parameters
from outputs import all_report_output_logic


logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def main():
    """
    :return: str
    """
    logging.info("Starting process")
    report_args = run_parameters()

    all_report_output_logic(report_args.principal,
                            report_args.payment,
                            report_args.interest,
                            report_args.periods,
                            report_args.type)


if __name__ == "__main__":
    main()
