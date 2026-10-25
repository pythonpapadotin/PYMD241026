print('hello world!')

#  Grammar - Syntax
# you will learn with time


# Data Types

# 1. int : 4, 5, -10, 23, -300. etc
# 2. float: 4.5, 50.32, -90.34, etc
# 3. bool: True, False
# 4. list: [4, 78.10, -90, True, False, 'nitin', 'pillai']
# 5. dict: {"python": 3.15, "java": 21.2, "pandas": 0.8} - key: value
# 6. set: {"python", "pandas", "java"} - unique
# 7. None : represents nothing/null
# 8. str: sequence of characters : "pandas", "nitin", "34342@#$@", etc
# 9. tuple: immutable/uneditable : (4, 78.10, -90, True, False, 'nitin', 'pillai')

# Variables/Names

# They are just names, and they do not represent the data
# type, they have nothing to do with data types.

person1_name = 'pillai'

person1_address = 'kerala'

person2_name = 'nitin'

person2_address = 'UP'

# snake case: small case words joined with an underscore

# Rules of naming variables:-
# 1 you can not start variable/name with a number
# 2 snake case is used for variable naming.
# 3 you are not allowed to use special characters

# 2person_name = 'nitin2'

_person_name = 'mango'

# type of data the variable is pointing to, you can use
# type() function

x = 56

print("x", type(x))

y = 'mango'

print("y", type(y))

z = ['mango', 'apple', 'banana']

print("z", type(z))

# Operators
# Airthmetic Operators :- +, -, *, /, //, %, **
sum_of_numbers = 4 + 50 + 49

print(sum_of_numbers)

x = 5/3

print("x is ", x)

y = 5//3

print("y is ", y)

# modulus operator %

z = 5 % 3

print("z is ", z)

# comparison operators

# comparing 2 things, whether they are equal, greater, lesster, etc
# comparison operator give you bool :True/False
x = 40
y = 10

result = x < y
result2 = x > y
result3 = x == y
result4 = x != y

print("result is ", result)

print("result2 is ", result2)

print("result3 is ", result3)

print("result4 is ", result4)

# and , or, not

x = True or False

print("x is ", x)

y = not True

print('y is ', y)

# assignment

x = 5

x += 2

print('x now is', x)

x *= 3

print('x after x*=3', x)

# membership operators

# in, not in
# gives you bool: True/False

list_of_fruits = ['apple', 'mango', 'banana', 'kiwi']

print("mango membership", 'mango' in list_of_fruits)

print("mango not membership", 'mango' not in list_of_fruits)
