import math


def calculate_nominal_interest(interest_rate: float) -> float:
    """
    Simple function to calculate nominal interest
    :param interest_rate: interest rate (APR)
    :return: nominal (monthly) interest rate
    """

    return interest_rate / (12 * 100)


def calculate_loan_principal(annuity_payment: float,
                             nominal_interest: float,
                             number_of_payments: int) -> dict:
    """
    Function to calculate the loan principal
    Returns a dict with both loan principal and overpayment amount
    :param annuity_payment: float: monthly payment amount
    :param nominal_interest: float: monthly interest amount
    :param number_of_payments: int: total payments for loan
    :return: dict: "loan_principal" "overpayment"
    """

    loan_principal = math.floor(annuity_payment / (nominal_interest *
                       (1 + nominal_interest) ** number_of_payments /
                       ((1 + nominal_interest) ** number_of_payments - 1)))
    overpayment = math.ceil(
        (annuity_payment * number_of_payments) - loan_principal)
    return {"loan_principal": loan_principal,
            "overpayment": overpayment}


def calculate_annuity_payment(loan_principal: int,
                              number_of_payments: int,
                              nominal_interest: float) -> dict:
    """
    Function to calculate the annuity payment
    Returns a dict with both annuity payment and overpayment amount
    :param loan_principal: int
    :param number_of_payments: int
    :param nominal_interest: int
    :return: dict: "annuity" "overpayment"
    """

    payment = math.ceil((
                nominal_interest *
                (1 + nominal_interest) ** number_of_payments / (
                        (1 + nominal_interest) ** number_of_payments - 1) *
                loan_principal))
    overpayment = math.ceil((payment * number_of_payments) - loan_principal)
    return {"annuity_payment": payment, "overpayment": overpayment}


def calculate_differential_payments(loan_principal: int,
                                    number_of_payments: int,
                                    nominal_interest: float) -> dict:
    """
    Function to calculate the differential payments
    Returns a dict with both diff payments list and overpayment amount
    :param loan_principal: int
    :param number_of_payments: int
    :param nominal_interest: int
    :return: dict: "diff_payments" "overpayment"
    """
    month = 1
    overpayment = 0
    payments = []

    for _ in range(number_of_payments):
        diff = (loan_principal / number_of_payments) + nominal_interest * (
                loan_principal - loan_principal * (month - 1) /
                number_of_payments)

        month_payment = (month, math.ceil(diff))
        payments.append(month_payment)
        overpayment += math.ceil(diff)
        month += 1

    overpayment = overpayment - loan_principal
    return {"diff_payments": payments, "overpayment": overpayment}


def calculate_number_of_payments(monthly_payment: int,
                                 nominal_interest: float,
                                 principal_amount: int) -> dict:
    """
    Function to calculate the total number of payments
    Returns a dict with both total years/months tuple and overpayment amount
    :param monthly_payment: int:
    :param nominal_interest: float:
    :param principal_amount: int:
    :return: dict: "years_months" "overpayment"
    """

    total_months = math.ceil(math.log(
        monthly_payment / (
                    monthly_payment - nominal_interest * principal_amount),
        (1 + nominal_interest)
    ))
    years, months = divmod(total_months, 12)
    overpayment = round(
        monthly_payment * math.ceil(total_months) - principal_amount)

    return {"years_months": [years, months],
            "overpayment": overpayment}
