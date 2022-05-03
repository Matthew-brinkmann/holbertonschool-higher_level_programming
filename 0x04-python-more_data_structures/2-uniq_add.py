#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_set = {ele for ele in my_list}
    num = sum(new_set)
    return num
