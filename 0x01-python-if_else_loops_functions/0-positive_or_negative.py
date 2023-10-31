#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    state = "zero"
elif number > 0:
    state = "positive"
else:
    state = "negative"
print(f"{number:d} is {state}")
