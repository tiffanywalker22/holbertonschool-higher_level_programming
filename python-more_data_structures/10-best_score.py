#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_key = max(a_dictionary, key=lambda k: a_dictionary[key])
        return (best_key)
    else:
        return (None)
