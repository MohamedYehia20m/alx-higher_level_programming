#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = number % 10
if number < 0:
    number2 -= 10
if number2 == 0:
    state = "and is 0"
elif number2 > 5:
    state = "and is greater than 5"
else:
    state = "and is less than 6 and not 0"
print(f"Last digit of {number:d} is {number2:d} {state}")
