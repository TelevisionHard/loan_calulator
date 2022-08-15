from typing import Optional
import logging
from loan_calculation_logic import (
    calculate_nominal_interest,
    calculate_loan_principal,
    calculate_differential_payments,
    calculate_annuity_payment,
    calculate_number_of_payments
)

log = logging.getLogger(__name__)


def format_month_to_year(years_months: list) -> str:
    """
    :param years_months: list
    :return: str
    """

    years = years_months[0]
    months = years_months[1]

    log.info("formatting month to year output")

    if years >= 1 and months == 0:
        return f"""
        It will take {years} years to repay this loan!
        """.lstrip()
    if years >= 1 and months >= 1:
        return f"""
        It will take {years} years and {months} months to repay this loan!
        """.lstrip()
    else:
        return f"""
        It will take {months} months to repay this loan!
        """.lstrip()


def format_annuity_amount(payment_amount: int) -> str:
    """
    :param payment_amount: int
    :return: str
    """

    log.info("formatting annuity output")
    return f"Your annuity payment {payment_amount}!"


def format_diff_payment_amount(month: int, diff_payment_amount: int) -> str:
    """
    :param month: int
    :param diff_payment_amount: int
    :return: str
    """

    log.info("formatting differential payment output")
    return f"Month {month}: payment is {diff_payment_amount}!"


def format_over_payment_amount(over_payment_amount: int) -> str:
    """
    :param over_payment_amount: int
    :return: str
    """

    log.info("formatting over payment output")
    return f"Overpayment = {over_payment_amount}"


def format_loan_principal(loan_principal: int) -> str:
    """
    :param loan_principal: int
    :return: str
    """

    log.info("formatting loan principal output")
    return f"Your loan principal = {loan_principal}!"


def diff_payment_output_logic(loan_principal: int,
                              number_of_periods: int,
                              loan_interest: float):
    nominal_int = calculate_nominal_interest(loan_interest)
    payments = calculate_differential_payments(loan_principal,
                                               number_of_periods,
                                               nominal_int)

    for v in payments["diff_payments"]:
        print(format_diff_payment_amount(v[0], v[1]))
    print(format_over_payment_amount(payments["overpayment"]))


def annuity_payment_output_logic(loan_principal: int,
                                 number_of_periods: int,
                                 loan_interest: float):

    nominal_int = calculate_nominal_interest(loan_interest)
    annuity_payments = calculate_annuity_payment(
        loan_principal,
        number_of_periods,
        nominal_int)
    print(format_annuity_amount(annuity_payments["annuity_payment"]))
    print(format_over_payment_amount(annuity_payments["overpayment"]))


def total_payments_output_logic(loan_principal: int,
                                monthly_payment: int,
                                loan_interest: float):

    nominal_int = calculate_nominal_interest(loan_interest)
    total_payments = calculate_number_of_payments(
        monthly_payment,
        nominal_int,
        loan_principal
    )
    print(format_month_to_year(total_payments["years_months"]))
    print(format_over_payment_amount(total_payments["overpayment"]))


def loan_principal_output_logic(monthly_payment: int,
                                number_of_periods: int,
                                loan_interest: float):
    nominal_int = calculate_nominal_interest(loan_interest)
    principal = calculate_loan_principal(
        monthly_payment,
        nominal_int,
        number_of_periods)

    print(format_loan_principal(principal["loan_principal"]))
    print(format_over_payment_amount(principal["overpayment"]))


def all_report_output_logic(
        loan_principal: Optional[int] = None,
        monthly_payment: Optional[int] = None,
        loan_interest: Optional[float] = None,
        number_of_periods: Optional[int] = None,
        payment_type: Optional[str] = None):
    """
     Function to filter down to an output type through parameter values

    :param loan_principal:
    :param monthly_payment:
    :param loan_interest:
    :param number_of_periods:
    :param payment_type:
    :return:
    """

    log.info("Starting report output logic")
    if payment_type == "diff":
        log.info("Starting differential payment")
        if loan_principal and number_of_periods and loan_interest:
            diff_payment_output_logic(loan_principal,
                                      number_of_periods,
                                      loan_interest)
        else:
            print("Incorrect parameters.")

    elif payment_type == "annuity":
        log.info("Starting annuity payment logic")
        if loan_principal and number_of_periods and loan_interest:
            annuity_payment_output_logic(loan_principal,
                                         number_of_periods,
                                         loan_interest)

        elif loan_principal and monthly_payment and loan_interest:
            log.info("Starting total annuity payments logic")
            total_payments_output_logic(loan_principal,
                                        monthly_payment,
                                        loan_interest)

        elif monthly_payment and number_of_periods and loan_interest:
            log.info("Starting loan principal logic")
            loan_principal_output_logic(monthly_payment,
                                        number_of_periods,
                                        loan_interest)
        else:
            print("Incorrect parameters.")

    else:
        print("Incorrect parameters.")
