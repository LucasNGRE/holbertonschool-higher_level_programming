#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_elements = set()
    for item in set_1:
        if item not in set_2:
            unique_elements.add(item)
    for item in set_2:
        if item not in set_1:
            unique_elements.add(item)
    return unique_elements
