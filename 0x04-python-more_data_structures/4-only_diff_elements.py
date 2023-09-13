#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    part1 = [x for x in set_1 if x not in set_2]
    part2 = [x for x in set_2 if x not in set_1]
    result = set(part1 + part2)
    return result
