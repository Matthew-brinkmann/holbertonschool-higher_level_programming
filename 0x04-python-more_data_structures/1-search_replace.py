#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = [ele if ele != search else replace for ele in my_list]
    return new_list
