from datetime import datetime, timedelta


users = [{"name": "Kolya", "birthday": datetime(year=2003, month=8, day=14)},
         {"name": "Timur", "birthday": datetime(year=2000, month=7, day=21)},
         {"name": "Kristian", "birthday": datetime(year=1997, month=8, day=14)},
         {"name": "Zhenya", "birthday": datetime(year=1999, month=12, day=31)},
         {"name": "Olga", "birthday": datetime(year=1999, month=7, day=28)},
         {"name": "Petya", "birthday": datetime(year=1999, month=7, day=29)},
         {"name": "Kira", "birthday": datetime(year=1999, month=7, day=30)},
         {"name": "Goose", "birthday": datetime(year=1999, month=7, day=31)},
         {"name": "Andrew", "birthday": datetime(year=1999, month=8, day=1)},
         {"name": "Helen", "birthday": datetime(year=1999, month=8, day=2)},
         {"name": "Ursula", "birthday": datetime(year=1999, month=8, day=3)},]


def get_birthday_celebration(birthdate: datetime, current_date=datetime.now()) -> datetime:
    current_year = current_date.year
    is_leap_year = True if current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0) else False
    if birthdate.day == 29 and birthdate.month == 2 and not is_leap_year:
        celebration_day = 1
        celebration_month = 3
    else:
        celebration_day = birthdate.day
        celebration_month = birthdate.month

    birthday_celebration = datetime(current_year, celebration_month, celebration_day)

    return birthday_celebration


def get_birthdays_per_week(users, current_date=datetime.now()) -> None:
    current_date = datetime(current_date.year, current_date.month, current_date.day)
    current_weekday = current_date.weekday()

    if current_weekday:
        start_date = current_date
        end_date = current_date + timedelta(days=7)
    else:
        start_date = current_date - timedelta(days=2)
        end_date = current_date + timedelta(days=5)

    users_birthday_list = {}

    for user in users:
        user_birthday = get_birthday_celebration(user["birthday"], current_date)

        if user_birthday - start_date < timedelta(days=7) and end_date - user_birthday < timedelta(days=8):
            if user_birthday.weekday() in (5, 6):
                user_weekday = 0
            else:
                user_weekday = user_birthday.weekday()

            users_birthday_list.setdefault(user_weekday, []).append(user["name"])

    weekday_names = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    for weekday, users in sorted(users_birthday_list.items()):
        print(f"{weekday_names[weekday]}: {', '.join(users)}")


if __name__ == '__main__':
    get_birthdays_per_week(users)