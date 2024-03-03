import datetime

year = int(input("Enter Persons birth year: "))
month = int(input("Enter Persons birth month(1-12): "))
day = int(input("Enter Persons birthday(1-31): "))
birth_date = datetime.date(year, month, day)
week_day = birth_date.strftime("%A")
print(f"Person was born on a {week_day}")
