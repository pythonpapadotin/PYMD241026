# Complete the given code such that we can verify if the sentence
# contains all the alphabets of english dictionary.
# 8: 45
def find_if_all_alphabets_are_present(sentence):
    alph = set("a$bcdefghijklmnopqrstuvwxyz")
    sen = set(sentence.lower())
    return alph.issubset(sen)


sentence1 = "the quick brown fox jumps over a lazy dog"
sentence2 = "the quick brown fox jumps over a dog"
# unit test1
assert find_if_all_alphabets_are_present(sentence1) is True

# unit test2
assert find_if_all_alphabets_are_present("quick red fox") is False

# unit test3
assert find_if_all_alphabets_are_present(sentence2) is False

print('All Passed')
