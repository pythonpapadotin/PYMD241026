def find_if_all_alphabets_are_present(sentence):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in sentence:
            return False
    return True
