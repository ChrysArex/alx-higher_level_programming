#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        max_ = list(a_dictionary.values())[0]
        best = list(a_dictionary.keys())[0]
        for i, j in a_dictionary.items():
            if j > max_:
                max_ = j
                best = i
        return best
