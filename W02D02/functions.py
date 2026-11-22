def join_and_create_sentence(list_of_words):
    sentence = " ".join(list_of_words)
    return sentence


sen1 = join_and_create_sentence(['apple', 'mango', 'orange'])

sen2 = join_and_create_sentence(['Hi', 'My', 'name', 'is', 'pillai'])

print('sen1', sen1)

print('sen2', sen2)


def add_two_numbers(a, b):
    return a + b


result1 = add_two_numbers(8, 90)

result2 = add_two_numbers(-9, 90)

print('result1', result1)
print('result2', result2)
