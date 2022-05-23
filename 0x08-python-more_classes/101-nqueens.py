#!/usr/bin/python3
"""
function to answer n-queens problem
"""
import sys

class Solutions_tracker:
    """ the solutions object"""

    savedGuess = []

    def __init__(self, row, col):
        self.__rowUsed = []
        self.__colUsed = []
        self.row_used = row
        self.col_used = col
        self.current_guess = [row, col]

    def __del__(self):
        Solutions_tracker.savedGuess = []
    @property
    def row_used(self):
        """ getter for row_used attribute"""
        return (self.__rowUsed)

    @row_used.setter
    def row_used(self, value):
        """ setter for row_used attribute"""
        self.__rowUsed.append(value)

    @property
    def col_used(self):
        """ getter for col_used attribute"""
        return (self.__colUsed)

    @col_used.setter
    def col_used(self, value):
        """ setter for col_used attribute"""
        self.__colUsed.append(value)

    @property
    def current_guess(self):
        """ getter for currenGuess attribute"""
        return (self.__currentGuess)

    @current_guess.setter
    def current_guess(self, value):
        """ setter for currentGuess attribute"""
        self.__currentGuess = value
        self.row_used = value[0]
        self.col_used = value[1]

    def reset(self, row, col):
        self.__rowUsed = []
        self.__colUsed = []
        self.row_used = row
        self.col_used = col
        self.current_guess = [row, col]

def sort_bad_rows(num, attempt, chess_board):
    i = 0

    if len(chess_board) == 0:
        return
    for j in attempt.row_used:
        i = 0
        while i < len(chess_board):
            try:
                if chess_board[i][0] == j:
                    chess_board.pop(i)
                    continue
            except IndexError:
                break
            i += 1
    for l in attempt.col_used:
        i = 0
        while len(chess_board) > 0:
            try:
                if chess_board[i][1] == l:
                    chess_board.pop(i)
                    continue
            except IndexError:
                break
            i += 1


def sort_diagonal(num, attempt, chess_board):
    pass


def build_chess_board(num):
    chess_board = []
    for i in range(num):
        for k in range(num):
            new_ele=[]
            new_ele.append(i)
            new_ele.append(k)
            chess_board.append(new_ele)
    return (chess_board)


args = sys.argv

if len(args) != 2:
    exit(1)
if not args[1].isdigit():
    print("N must be a number")
    exit(1)

num = int(args[1])
if num < 4:
    print("N must be at least 4")
    exit(1)

for guess in range(num):
    chess_board = build_chess_board(num)
    attempt = Solutions_tracker(0, guess)
    while len(attempt.savedGuess) <= num:
        attempt.savedGuess.append(attempt.current_guess)
        sort_bad_rows(num, attempt, chess_board)
        sort_diagonal(num, attempt, chess_board)
        if len(chess_board) == 0:
            break
        else:
            attempt.current_guess = chess_board[0]
    if len(attempt.savedGuess) == num:
        print(attempt.savedGuess)
    attempt.savedGuess = []

# still need to program the diagonal search function
#[x++, y++] and [x++, y--] and [x--, y++] and [x--, y--]
#^^^ there may and probably is an easer way to do this^^^

#print any solution that has a len(guess) == num

#- if the left over len of matrix is greater than or equal to num iterate to next matrix spot
#- re-run tests
#- else
#- delete matrix and start again.
