#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    score = 0
    key = ""
    count = 0
    for k, v in a_dictionary.items():
        if count == 0:
            score = v
        if v > score:
            key = k
        score = v
        count += 1
    if key == '':
        return None
    return key
