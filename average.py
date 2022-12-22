#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Dec 2022
# This program calculates the average between numbers

import random


def main():
    # this unction uses an array
    answer = 0

    random_numbers = []
    # process
    for loop_counter in range(0, 10):
        a_random_number = random.randint(1, 100)  # a number between 1 and 100
        print("Random number is: {0}".format(a_random_number))
        random_numbers.append(a_random_number)
    print("")

    for loop_counter in range(0, len(random_numbers)):
        answer = answer + random_numbers[loop_counter]
    average = answer / len(random_numbers)

    print("\nYour average is: {0}".format(average))


if __name__ == "__main__":
    main()
