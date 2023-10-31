#!/usr/bin/python3
def print_last_digit(number):
    number2 = number % 10
    if number < 0:
        number2 -= 10
        number2 *= -1
    print("{:d}".format(number2), end="")
    return number2
