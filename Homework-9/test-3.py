from datetime import datetime


str_date = input("Enter year-month-day-minute-second-ms-timezone: ")
print(str_date)

input_date = datetime.strptime(str_date, "%Y-%m-%dT%H:%M:%S.%f%z")
timezone = input_date.strftime("%z")
timezone_offset = timezone[0:3:2]

if int(timezone[1]) > 0:
    timezone_offset = timezone[0:3]

output_date = input_date.strftime("%d-%m-%Y %I:%M:%S ") + timezone_offset

print("Converted:", output_date)
