from test_1 import gcd_iterative


# Find lcm
def lcm(a, b):
    return (a * b) // gcd_iterative(a, b)


def main():
    a = int(input("Enter first number (0 to 10000): "))
    b = int(input("Enter second number (0 to 10000): "))

    if not (0 < a <= 10000 and 0 < b <= 10000):
        print("Please enter number up to 10000.")
        return

    result = lcm(a, b)
    print(f"LCM of {a} and {b} is {result}")


if __name__ == "__main__":
    main()
