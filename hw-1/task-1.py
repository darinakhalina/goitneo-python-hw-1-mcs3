from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users: list[dict]):
    # create empty list
    birthdays = defaultdict(list)
    today = datetime.now().date()

    for user in users:
        name = user["name"]
        # convert date
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1
            )

        # if the day of the week is Saturday
        if birthday_this_year.weekday() == 5:
            # moves birthday to the following Monday
            birthday_this_year += timedelta(days=2)
        # if the day of the week is Sunday
        elif birthday_this_year.weekday() == 6:
            # moves birthday to the following Monday
            birthday_this_year += timedelta(days=1)

        delta_days = (birthday_this_year - today).days
        if delta_days > 0 and delta_days <= 7:
            birthdays[birthday_this_year].append(name)

    if len(birthdays) == 0:
        print("No birthdays found")

    # sort birthdays
    sorted_birthdays = sorted(birthdays.keys())

    for day in sorted_birthdays:
        print(f"{day.strftime('%A')}: {', '.join(birthdays[day])}")
