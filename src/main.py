from parameters import run_parameters
from outputs import all_report_output_logic


def main():
    """
    :return: str
    """
    report_args = run_parameters()
    all_report_output_logic(report_args.principal,
                            report_args.payment,
                            report_args.interest,
                            report_args.periods,
                            report_args.type)


if __name__ == "__main__":
    main()
