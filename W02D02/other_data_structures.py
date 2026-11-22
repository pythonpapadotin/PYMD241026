# Sets
# unordered
# remove duplicates
# math set operations
# mutable
# sets are like keys of dicts: unique (hashing)

list_of_fruits = ['apple', 'mango', 'orange', 'orange']
print('len of list', len(list_of_fruits))
set_of_fruits = set(list_of_fruits)

print(type(set_of_fruits))
print(set_of_fruits)
print('len of set', len(set_of_fruits))

set_of_fruits.add('kiwi')

print(set_of_fruits)
print('len of set', len(set_of_fruits))

set_of_fruits.add('apple')
print(set_of_fruits)
print('len of set', len(set_of_fruits))

A = {1, 2, 3}
B = {4, 5, 6, 1}

C = A.union(B)
print(C, type(C))

D = A.intersection(B)

print("D", D, type(D))

E = A.difference(B)
print("E", E, type(E))

# Tuple
# they are very similar to list hetro, indexing, ordered, slicing
# tuples are immutable/uneditable

x = ('A', 'B', 12, 34, True, False, 'apple', None, 34.56)
print(x, type(x))

print("At 0th index we have", x[0])

# uncomment to see error on tuple
# x[0] = 'shyam'


# tuple unpacking

x = "mango", 'orange', 234, 456.89
print('X--->', x, type(x))
a1, a2, a3, a4 = "mango", 'orange', 234, 456.89
print('a1', a1)
print('a2', a2)
print('a3', a3)
print('a4', a4)

# str
# sequnce of characters
# mango
# ordered, indexing, slicing
name = 'dele'
# name[0] = 'm'

# StringBuilder concept in C#
x = []

for i in range(1, 9):
    x.append("BlaBla" + str(i))

number_sentence = " ".join(x)
print('number_sentence', number_sentence)


list_of_words = ['Hi', 'My', 'name', 'is', 'mohit']

sentence = " ".join(list_of_words)

print('sentence', sentence)

words = sentence.split(" ")

print('words', words, type(words))


