import random


def cels_to_fahr(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def fahr_to_cels(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def main():
    cels_temp = [random.randint(-50, 60) for _ in range(5)]
    fahr_temp = [random.randint(-60, 134) for _ in range(5)]

    print("Celsius to Fahrenheit:")
    for celsius in cels_temp:
        fahrenheit = cels_to_fahr(celsius)
        print(f"{celsius}C = {fahrenheit:.1f}F")

    print("\nFahrenheit to Celsius")
    for fahrenheit in fahr_temp:
        celsius = fahr_to_cels(fahrenheit)
        print(f"{fahrenheit}F = {celsius:.1f}C")


if __name__ == "__main__":
    main()
