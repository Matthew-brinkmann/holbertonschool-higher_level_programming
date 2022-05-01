#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tup = ()
    for i in range(2):
        if i >= len(tuple_a):
            val1 = 0
        else:
            val1 = tuple_a[i]

        if i >= len(tuple_b):
            val2 = 0
        else:
            val2 = tuple_b[i]

        if i == 0:
            new_tup = (val1 + val2)
        else:
            new_tup = (new_tup, (val1 + val2))

    return (new_tup)
