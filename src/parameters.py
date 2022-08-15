import argparse
import logging

log = logging.getLogger(__name__)


def run_parameters():
    """
    Function to collect parameters and returns a parser object
    :return: Callable
    """
    log.info("Collecting run parameters")
    parser = argparse.ArgumentParser(description="Loan calculator inputs")

    parser.add_argument(
        "--principal",
        required=False,
        type=int,
        help="""Total loan amount"""
    )

    parser.add_argument(
        "--payment",
        required=False,
        type=int,
        help="""Monthly payment amount"""
    )

    parser.add_argument(
        "--interest",
        required=False,
        type=float,
        help="""Interest rate"""
    )

    parser.add_argument(
        "--periods",
        required=False,
        type=int,
        help="""Total periods in months"""
    )

    parser.add_argument(
        "--annuity",
        required=False,
        type=int,
        help="""Annuity amount"""
    )

    parser.add_argument(
        "--type",
        required=False,
        type=str,
        help="""Type of payment:
                diff or annuity"""
    )

    args = parser.parse_args()
    return args
