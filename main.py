import datetime
from typing import Dict

from input_utils import date_input, float_input, optional_date_input, optional_float_input
from loan_classes import LoanCalculation, LoanInput, DailyInterest

calculations: Dict[int, LoanCalculation] = {}


def calculate_interest(loan_input: LoanInput) -> LoanCalculation:
    """
    Calculates interest breakdown and provides a detailed daily calculation of interest
    for a given loan input over a specified period.


    :param loan_input: LoanInput object including amount, base interest rate, margin,
        start date, and end date
    :return: LoanCalculation object including daily breakdowns and
        total interest accrued
    """

    # Calculate the number of days between start and end dates, inclusive
    days = (loan_input.end_date - loan_input.start_date).days + 1
    base_rate_daily = loan_input.base_interest_rate / 100 / 365
    total_rate_daily = (loan_input.base_interest_rate + loan_input.margin) / 100 / 365
    daily_base = loan_input.amount * base_rate_daily
    daily_total = loan_input.amount * total_rate_daily

    daily_results = []
    total_interest = 0.0

    for day_offset in range(days):
        accrual_date = loan_input.start_date + datetime.timedelta(days=day_offset)
        total_interest += daily_total

        daily_results.append(
            DailyInterest(
                daily_interest_base=daily_base,
                daily_interest_total=daily_total,
                accrual_date=accrual_date,
                days_elapsed=day_offset,
                accrued_interest=round(total_interest, 2),
            )
        )

    return LoanCalculation(
        input=loan_input,
        daily_results=daily_results,
        total_interest=round(total_interest, 2),
    )


def create_new_loan():
    start_date = date_input("Enter Start Date (YYYY-MM-DD): ")
    end_date = date_input("Enter End Date (YYYY-MM-DD): ")
    if start_date > end_date:
        print("Start date cannot be after end date.")
        return
    loan_amount = float_input("Enter Loan Amount: ")
    loan_currency = input("Enter Loan Currency: ")
    base_rate = float_input("Enter Base Interest Rate (%): ")
    margin = float_input("Enter Margin (%): ")

    loan_input = LoanInput(start_date, end_date, loan_amount, loan_currency, base_rate, margin)
    calculation = calculate_interest(loan_input)
    calculation_id = len(calculations) + 1
    calculations[calculation_id] = calculation

    print(f"\nLoan Calculation ID: {calculation_id}")
    calculation.print_output()


def view_existing_loans():
    if not calculations:
        print("No previous calculations found.")
        return

    for calc_id, calc in calculations.items():
        print(f"\nLoan Calculation ID: {calc_id}, ", end="")
        calc.print_input()


def update_existing_loan():
    loan_id = int(input("Enter Loan ID to update: "))
    if loan_id not in calculations:
        print("Loan ID not found.")
        return

    print("Enter new values (leave blank to keep current value):")
    old_input = calculations[loan_id].input

    start_date = optional_date_input(f"Start Date [{old_input.start_date}]: ", default=old_input.start_date)
    end_date = optional_date_input(f"End Date [{old_input.end_date}]: ", default=old_input.end_date)
    if start_date > end_date:
        print("Start date cannot be after end date.")
        return
    amount = optional_float_input(f"Amount [{old_input.amount}]: ", default=old_input.amount)
    currency = input(f"Currency [{old_input.currency}]: ") or old_input.currency
    base_rate = optional_float_input(
        f"Base Interest Rate (%) [{old_input.base_interest_rate}]: ", default=old_input.base_interest_rate
    )
    margin = optional_float_input(f"Margin (%) [{old_input.margin}]: ", default=old_input.margin)

    updated_input = LoanInput(
        start_date=start_date,
        end_date=end_date,
        amount=amount,
        currency=currency,
        base_interest_rate=base_rate,
        margin=margin,
    )

    new_calculation = calculate_interest(updated_input)
    calculations[loan_id] = new_calculation

    print("\nUpdated Loan Calculation:")
    new_calculation.print_output()


def main():
    while True:
        print("\nWelcome to the Loan Interest Calculator!")
        print("1. New Loan")
        print("2. View Past Loans")
        print("3. Update Loan")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_new_loan()
        elif choice == "2":
            view_existing_loans()
        elif choice == "3":
            update_existing_loan()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
