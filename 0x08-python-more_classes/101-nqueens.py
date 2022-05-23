#!/usr/bin/python3
"""
function to answer n-queens problem
"""
from sys import argv

class Solutions_tracker:
    """ the solutions object"""
    row_used = []
    col_used = []

    def __init__(self, row, col):
        self.row_used = row
        self.col_used = col

    @property
    def row_used(self):
        """ getter for row_used attribute"""
        return (self.__rowUsed)

    @width.setter
    def row_used(self, value):
        """ setter for row_used attribute"""
        self.__rowUsed = __rowUsed.append(value)

    @property
    def col_used(self):
        """ getter for col_used attribute"""
        return (self.__colUsed)

    @width.setter
    def col_used(self, value):
        """ setter for col_used attribute"""
        self.__colUsed = __colUsed.append(value)

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


chess_board = []
for i in range(num):
    for k in range(num):
        new_ele=[]
        new_ele.append(i)
        new_ele.append(k)
        chess_board.append(new_ele)
#- create the matix with all numbers [0 , 0] to [num, num]
print(chess_board)
# put this in a loop to loop through all initial guess stage (0,0 -> 0, num)
guess_stage = 0
attempt = Solutions_tracker(0, guess_stage)
# check if row or column has the guess numbers in it
while len(chess_board) > 0:
    if (len(chess_board) <= i):
        break
    for j in col:
        for test in range(num):
            if chess_board[i] == [j, test]:
                chess_board.pop(i)
    for l in row:
        for test1 in range(num):
            if chess_board[i] == [test1, l]:
                chess_board.pop(i)
    i += 1
# still need to program the diagonal search function
#[x++, y++] and [x++, y--] and [x--, y++] and [x--, y--]
#^^^ there may and probably is an easer way to do this^^^

#print any solution that has a len(guess) == num

#- if the left over len of matrix is greater than or equal to num iterate to next matrix spot
#- re-run tests
#- else
#- delete matrix and start again.
