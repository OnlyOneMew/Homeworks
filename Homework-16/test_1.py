def calc_average_temperature(temperatures):
    total_temp = sum(temperatures)
    temp_length = len(temperatures)
    average_temp = total_temp / temp_length
    return average_temp


def main():
    temperatures = [22, 25, 19, 23, 25, 26, 23]
    average_temp = calc_average_temperature(temperatures)
    print(f"Average temperature: {average_temp:.0f}")


if __name__ == "__main__":
    main()
