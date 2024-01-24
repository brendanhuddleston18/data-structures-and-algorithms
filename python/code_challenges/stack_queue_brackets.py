from data_structures.queue import Queue


def multi_bracket_validation(string):
    bracket_list = []

    bracket_dictionary = {
        "}":"{",
        ")":"(",
        "]":"["
    }

    for char in string:
        if char in bracket_dictionary.values():
            bracket_list.append(char)
        # Kyle helped with the checking of the values
        elif bracket_list and bracket_dictionary[char] == bracket_list[-1]:
            bracket_list.pop()
        else:
            return False
    
    if bracket_list == []:
        return True
    else: 
        return False
        
