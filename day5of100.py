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
    def initial_tile():
        top = '   ' + chr(95) + chr(40) + ' ' + chr(41) + chr(95) + chr(95) + '\n'
        middle = chr(95) + chr(124) + '     ' + chr(95) + chr(124) + '\n' + chr(40) + chr(95) + '   ' + chr(95) + ' ' + chr(40) + chr(95) + '\n'
        bottom = chr(124) + chr(95) + chr(95) + chr(40) + ' ' + chr(41) + chr(95) + chr(124)
        first_piece = " ".join([top, middle, bottom])
        print(first_piece)
        return first_piece
    def horizontal_tiles():
        top_row = '   ' + chr(95) + chr(40) + ' ' + chr(41) + chr(95) + chr(95)
        next_top_piece = ''
        second_row = '\n' + ' ' + chr(95) + chr(124) + '     ' + chr(95) + chr(124)
        next_second_row = ''
        third_row = '\n' + chr(40) + chr(95) + '   ' + chr(95) + ' ' + chr(40) + chr(95)
        next_third_row = ''
        last_row = '\n' + ' ' + chr(124) + chr(95) + chr(95) + chr(40) + ' ' + chr(41) + chr(95) + chr(124)
        next_last_row = ''
        for piece in range(width-1):
            next_top_piece += ' ' + chr(95) + chr(40) + ' ' + chr(41) + chr(95) + chr(95)
            next_second_row += '     ' + chr(95) + chr(124)
            next_third_row += '   ' + chr(95) + ' ' + chr(40) + chr(95)
            next_last_row += ' ' + chr(95) + chr(40) + ' ' + chr(41) + chr(95) + chr(124)

        print(top_row + next_top_piece + second_row + next_second_row + third_row + next_third_row + last_row +
              next_last_row)
        horizontal_pieces = top_row + next_top_piece + second_row + next_second_row + third_row + next_third_row + \
                            last_row + next_last_row
        return horizontal_pieces
    if width == 1 and height == 1:
        return initial_tile()
    else:
        return horizontal_tiles()



puzzle_tiles(6,1)

'   _( )__ _( )__ _( )__\n _|     _|     _|     _|\n(_   _ (_   _ (_   _ (_\n |__( )_| _( )_| _( )_|' should equal
'   _( )__ _( )__ _( )__\n _|     _|     _|     _|\n(_   _ (_   _ (_   _ (_\n |__( )_|__( )_|__( )_|\n |_     |_     |_     |_\n  _) _   _) _   _) _   _)\n |__( )_|__( )_|__( )_|'
