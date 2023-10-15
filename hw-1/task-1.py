from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users: list[dict]):
    birthdays = defaultdict(list)
    today = datetime.now().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1
            )

        if birthday_this_year.weekday() == 5:
            birthday_this_year += timedelta(days=2)
        elif birthday_this_year.weekday() == 6:
            birthday_this_year += timedelta(days=1)

        delta_days = (birthday_this_year - today).days
        if delta_days > 0 and delta_days <= 7:
            birthdays[birthday_this_year].append(name)

    if len(birthdays) == 0:
        print("No birthdays found")

    sorted_birthdays = sorted(birthdays.keys())

    for day in sorted_birthdays:
        print(f"{day.strftime('%A')}: {', '.join(birthdays[day])}")
