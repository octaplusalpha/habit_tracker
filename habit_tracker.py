from datetime import datetime
from dataclasses import dataclass

from pandas.core.util.numba_ import maybe_use_numba


@dataclass
class Habit:
    name: str
    elapsed_time: str
    remaining_time: str
    minutes_saved: float
    money_saved: str


def track_habit(name: str, start_time: datetime, cost: float, minutes_used: float) -> Habit:
    goal: int = 60
    hourly_wage: float = 30
    elapsed_time: float = (datetime.now() - start_time).total_seconds()
    hours: float = round(elapsed_time / 60 / 60, 1)
    days: float = round(hours / 24, 1)
    money_saved: float = cost * days
    minutes_used: float = round(days * minutes_used, 2)
    total_money_saved: str = f'₦{round(money_saved + (minutes_used / 60) * hourly_wage, 2)}'
    days_to_go: float | str = round(goal - days)
    remaining_days: str = "Cleared" if days_to_go <=0 else f'{days_to_go} days'
    time_since: str = f"{days}days" if hours > 72 else f"{hours}hours"
    return Habit(name, time_since, remaining_days, minutes_used, total_money_saved)


def get_info():
    valid = False
    while True:
        while True:
            habit: str = input("Habit: ")
            if habit.isalpha():
                habit = habit
                break
            else:
                print("Please State a Proper Habit")
                continue

        while True:
            start_time = dict()
            start_time["year"] = input("year: ")

            if start_time["year"].isdigit() and 1900 <= int(start_time["year"]) <= datetime.now().year:
                start_time["year"] = int(start_time["year"])
                break
            else:
                print("Please Enter a valid Year")
                continue


        while True:
            start_time["month"] = input("month: ")
            if start_time["month"].isdigit() and 0 < int(start_time["month"]) <= 12:
                start_time["month"] = int(start_time["month"])
                break
            else:
                print("Please Enter a valid Month")
                continue

        while True:
            start_time["day"] = input("day: ")
            if start_time["day"].isdigit() and 0 < int(start_time["day"]) <= 31:
                start_time["day"] = int(start_time["day"])
                break
            else:
                print("Please Enter a valid Day")
                continue

        while True:
            start_time["hour"] = input("hour: ")
            if start_time["hour"].isdigit() and 0 < int(start_time["hour"]) <= 24:
                start_time["hour"] = int(start_time["hour"])
                break
            else:
                print("Please Enter a valid Hour")
                continue

        while True:
            cost: str | float = input("cost: ")
            if cost.isdigit():
                cost = float(cost)
                break
            else:
                print("Please Enter a valid Cost")
                continue

        while True:
            minutes_used: str | float = input("minutes used: ")
            if minutes_used.isdigit() and 0 < int(minutes_used) <= 1440:
                minutes_used = float(minutes_used)
            else:
                print("Enter valid Minutes used")
                continue

            start_point = datetime(**start_time)
            return habit, start_point, cost, minutes_used

if __name__ == '__main__':
    print(get_info())