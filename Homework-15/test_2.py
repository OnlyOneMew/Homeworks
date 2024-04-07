import random


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    for num in random_numbers:
        if is_prime(num):
            print(f"{num} is prime")
        else:
            print(f"{num} is not prime")


if __name__ == "__main__":
    main()
