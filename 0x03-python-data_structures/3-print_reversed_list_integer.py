#!/bin/usr/python3

def print_reversed_list_integer(my_list=[]):
    new_list = my_list[0:]
    new_list.reverse()
    for i in range(len(new_list)):
        print(f"{new_list[i]}")