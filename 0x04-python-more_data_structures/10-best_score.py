#!/usr/bin/python3

def best_score(a_dictionary):
    winner = None
    if type(a_dictionary) is dict:
        winner = max(a_dictionary, key=a_dictionary.get)
    return winner
