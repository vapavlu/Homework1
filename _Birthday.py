from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if days_until_birthday <= 7:
            if birthday_this_year.weekday() >= 5:  # якщо день припадає на вихідний
                days_until_birthday += 7 - birthday_this_year.weekday()
                birthday_this_year += timedelta(days=7 - birthday_this_year.weekday())

            congratulation_date = birthday_this_year.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date})

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "Іван", "birthday": "1990.05.04"},#день народження в суботу
    {"name": "Марія", "birthday": "1987.05.02"},
    {"name": "Петро", "birthday": "1995.04.25"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print(upcoming_birthdays)
