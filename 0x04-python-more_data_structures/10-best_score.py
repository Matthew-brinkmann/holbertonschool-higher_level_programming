#!/usr/bin/python3

def best_score(a_dictionary):
    winner = None
    highScore = 0
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > highScore:
                highScore = value
                winner = key
    return winner
