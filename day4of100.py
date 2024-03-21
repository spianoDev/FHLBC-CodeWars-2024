# Source https://www.codewars.com/kata/5e28b3ff0acfbb001f348ccc/train/python

# Given a board of NxN, distributed with tiles labeled 0 to N² - 1(inclusive):
#
# A solved grid will have the tiles in order of label, left to right, top to bottom.
#
# Return true if the board state is currently solved, and false if the board state is unsolved.
#
# Input will always be a square 2d array.
#
# For example, a 2x2 solved grid:
#
# [ [0, 1],
#   [2, 3] ]
# A 2x2 unsolved grid:
#
# [ [2, 1],
#   [0, 3] ]

def is_solved(board):
    count = 0
    for pair in board:
        if pair[0] == count and pair[1] == (count + 1):
            count += 2
        else:
            print('false')
            return False
    print('true')
    return True
is_solved([[0,1],[2,3]]) # => True
is_solved([[1,0],[3,2]]) # => False
