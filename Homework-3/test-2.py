import datetime

input_year = input("Enter Persons birth year: ")
input_month = input("Enter Persons birth month(1-12): ")
input_day = input("Enter Persons birthday(1-31): ")

if input_year.isdigit() and input_month.isdigit() and input_day.isdigit():
    year = int(input_year)
    month = int(input_month)
    day = int(input_day)

    if 1 <= month <= 12 and 1 <= day <= 31:
        birth_date = datetime.date(year, month, day)
        week_day = birth_date.strftime("%A")
        print(f"Person was born on a {week_day}")
    else:
        print("Please enter valid dates")
else:
    print("PLEASE ENTER DATE ONLY IN NUMBERS")