#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    state = "is zero"
elif number > 0:
    state = "is positive"
else:
    state = "is negative"
print(f"{number:d} is {state}")
