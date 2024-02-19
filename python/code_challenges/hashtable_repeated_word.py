from data_structures.hashtable import Hashtable
import re


def first_repeated_word(string):
    if string == "":
        return None

    hashtable = Hashtable()

    # word_list = string.split(" ")
    # print(word_list)
    word_list = re.findall(r'\b[a-zA-Z]+\b', string)
    for word in word_list:
        if hashtable.has(word.lower()):
            return word.lower()
        hashtable.set(word.lower(), word)
    return None

