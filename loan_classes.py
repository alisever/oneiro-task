import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class LoanInput:
    start_date: datetime.date
    end_date: datetime.date
    amount: float
    currency: str
    base_interest_rate: float  # in percentage
    margin: float  # in percentage

    def __str__(self):
        return (
            f"Start Date: {self.start_date}, "
            f"End Date: {self.end_date}, "
            f"Amount: {self.currency}{self.amount:.2f}, "
            f"Base Interest Rate: {self.base_interest_rate}%, "
            f"Margin: {self.margin}%"
        )


@dataclass
class DailyInterest:
    daily_interest_base: float
    daily_interest_total: float
    accrual_date: datetime.date
    days_elapsed: int
    accrued_interest: float

    def __str__(self):
        return (
            f"Base Daily Interest: {self.daily_interest_base:.5f}, "
            f"Total Daily Interest: {self.daily_interest_total:.5f}, "
            f"Accrual Date: {self.accrual_date}, "
            f"Days Elapsed: {self.days_elapsed}, "
            f"Accrued Interest: {self.accrued_interest:.2f}"
        )


@dataclass
class LoanCalculation:
    input: LoanInput
    daily_results: List[DailyInterest]
    total_interest: float

    def print_input(self):
        print(self.input)

    def print_output(self):
        print(f"Loan Amount: {self.input.currency}{self.input.amount:.2f}")
        print(f"Base Interest Rate: {self.input.base_interest_rate}%")
        print(f"Margin: {self.input.margin}%")
        print(f"Total Interest: {self.input.currency}{self.total_interest:.2f}")
        print("Daily Interest Accruals:")
        for result in self.daily_results:
            print("   ", result)
