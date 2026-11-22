def find_if_all_alphabets_are_present(sentence):
    alph = set("abcdefghijklmnopqrstuvwxyz")
    sen = set(sentence.lower())
    return alph.issubset(sen)
