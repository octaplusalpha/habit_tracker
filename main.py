import pandas
from tabulate import tabulate
from habit_tracker import track_habit,  Habit, get_info

def main():
    name, date, cost, minutes_used = get_info()
    habits: [Habit] = [
        track_habit(name, date, cost, minutes_used),
    ]
    df = pandas.DataFrame(habits)
    print(tabulate(df, headers="keys", tablefmt="psql"))

if __name__ == "__main__":
    main()