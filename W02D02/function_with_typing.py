import typing


def add_two_numbers(a: int, b: int) -> typing.Any(int, None):
    if type(a) == int and type(b) == int:
        return a + b
    return None


result = add_two_numbers("mango", 'orange')

print('result', result)
