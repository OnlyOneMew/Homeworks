input_speed = float(input("Enter Car speed in KM/h: "))
if 30 < input_speed <= 60:
    print("Your car is Moderate")
elif 60 <= input_speed <= 120:
    print("Your car is Fast")
elif input_speed > 120:
    print("Your car is Very fast")
else:
    print("Your car is too Slow")
