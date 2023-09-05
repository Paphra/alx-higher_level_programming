#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
_abs = number
if (number < 0):
    _abs *= -1
last_digit = _abs % 10
if (number < 0):
    last_digit *= -1
print(f"Last digit of {number} is {last_digit}", end=" ")
if (last_digit > 5):
    print("and is greater than 5")
elif (last_digit == 0):
    print("and is 0")
else:
    print("and is less than 6 and not 0")
