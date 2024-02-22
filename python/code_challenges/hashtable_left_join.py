from data_structures.hashtable import Hashtable


def left_join(syns, ants):

    word_list = []

    for key in syns:
        if key not in ants:
            word_list.append([key, syns[key], None])
        else:
            word_list.append([key, syns[key], ants[key]])

    return word_list
