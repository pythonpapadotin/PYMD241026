import numpy
import math


# Optional Argument
# Default Argument: The value which will be used if you don't pass anything
def greet(first_name, last_name=None):
    sentence = f"Hello {first_name}"
    if last_name is not None:
        sentence += " "
        sentence += last_name
    return sentence


result1 = greet('shyam')
print(result1)

result2 = greet('pillai', 'padmanabh')
print(result2)


def add_two_number(a, b=10):
    return a + b


result3 = add_two_number(2)
print('result3', result3)

result4 = add_two_number(b=20, a=30)
print('result4', result4)


# *args -> tuple


def add_numbers(*args):
    sum_of_numbers = sum(args)
    print(type(args), args)
    return sum_of_numbers


result5 = add_numbers(12, 34, 6700)
print("result5-->", result5)

result6 = add_numbers(1, 46, -100)
print("result6-->", result6)


# ** kwargs -> dict
def find_highest_marks(**kwargs):
    print(type(kwargs), kwargs)


find_highest_marks(shyam=99, mohit=78, pillai=59, nitin=100, romeo=79)

find_highest_marks(rohan=29, reddy=39)
