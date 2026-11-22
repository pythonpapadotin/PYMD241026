# Properties of dicts
# keys are unique
# keys are allowed to have only immutable data types
# value can be any data type
# they are not ordered and hence no indexing




# Why keys are immutable only?
# : keys needs to be hashed
# hashing takes a value and convert it into other form and is widely
# used for cryptography, security, etc etc

# "mango" -> "2349kldf"
# "mongo" -> "y349kldf"

marks_of_subjects = {
    'maths': 98,
    'english': 77,
    'hindi': 88,
    'french': 56
}

for item in marks_of_subjects.items():
    print(item[0], "--->", item[1])

# uncomment and it will give error
# new_dict = {
#     ['a', 'b', 'c']: "mango"
# }

new_dict = {
    ('a', 'b', 'c'): "mango"
}

print(new_dict)

print("marks_of_subjects of maths", marks_of_subjects['maths'])

print("marks_of_subjects of maths", marks_of_subjects.get('maths'))


# if the key is absent, marks_of_subjects[key] will give error while
# marks_of_subjects.get(key) will give None

