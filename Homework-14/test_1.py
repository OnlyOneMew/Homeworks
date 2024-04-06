# Find GCD iterative
def gcd_iterative(a, b):
    while b:
        a, b = b, a % b
    return a


# Find GCD recursive
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def main():
    a = int(input("Enter first number (0 to 10000): "))
    b = int(input("Enter second number (0 to 10000): "))

    if not (0 < a <= 10000 and 0 < b <= 10000):
        print("Please enter number up to 10000.")
        return

    gcd_iter = gcd_iterative(a, b)
    gcd_recur = gcd_recursive(a, b)
    print(f"GCD of {a} and {b} is {gcd_iter}")
    print(f"GCD of {a} and {b} is {gcd_recur}")


if __name__ == "__main__":
    main()
