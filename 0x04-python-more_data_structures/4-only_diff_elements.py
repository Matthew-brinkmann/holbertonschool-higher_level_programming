#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set = {ele for ele in (set_1 | set_2) if ele in set_1 and
               ele not in set_2 or ele in set_2 and ele not in set_1}

    return new_set
