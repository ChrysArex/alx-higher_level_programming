#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_del = []
    if value in a_dictionary.values():
        for key in a_dictionary.keys():
            if a_dictionary[key] == value:
                to_del.append(key)
        for i in to_del:
            del a_dictionary[i]
    return a_dictionary
