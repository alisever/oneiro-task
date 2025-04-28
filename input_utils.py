import datetime


def date_input(prompt: str) -> datetime.date:
    while True:
        try:
            date_str = input(prompt)
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def optional_date_input(prompt: str, default: datetime.date) -> datetime.date:
    while True:
        date_str = input(prompt)
        if not date_str:
            return default
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def optional_float_input(prompt: str, default: float) -> float:
    while True:
        value_str = input(prompt)
        if not value_str:
            return default
        try:
            return float(value_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
