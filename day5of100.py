# Source https://www.codewars.com/kata/5947d86e07693bcf000000c4/train/python

# You will get two Integer n(width) and m (height) and your task is to draw following pattern. Each line is seperated with '\n'.
#
# Both integers are equal or greater than 1. No need to check for invalid parameters.
# There are no whitespaces at the end of each line.
# For example, for width = 4 and height = 3, you should draw the following pattern:
#
#    _( )__ _( )__ _( )__ _( )__
#  _|     _|     _|     _|     _|
# (_   _ (_   _ (_   _ (_   _ (_
#  |__( )_|__( )_|__( )_|__( )_|
#  |_     |_     |_     |_     |_
#   _) _   _) _   _) _   _) _   _)
#  |__( )_|__( )_|__( )_|__( )_|
#  _|     _|     _|     _|     _|
# (_   _ (_   _ (_   _ (_   _ (_
#  |__( )_|__( )_|__( )_|__( )_|

def puzzle_tiles(width, height):
    def tile1():
        top = '   ' + chr(95) + chr(40) + ' ' + chr(41) + chr(95) + chr(95) + '\n'
        middle = chr(95) + chr(124) + '     ' + chr(95) + chr(124) + '\n' + chr(40) + chr(95) + '   ' + chr(95) + ' ' + chr(40) + chr(95) + '\n'
        bottom = chr(124) + chr(95) + chr(95) + chr(40) + ' ' + chr(41) + chr(95) + chr(124)
        first_piece = " ".join([top, middle, bottom])
        print(first_piece)
        return first_piece
    return tile1()

puzzle_tiles(1,1)
