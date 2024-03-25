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
        # print(first_piece, 'first piece')
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
    def first_vertical_tile():
        top_row = '\n' + ' ' + chr(124) + chr(95) + '     ' + chr(124) + chr(95) +  '\n'
        middle_row = '  ' + chr(95) + chr(41) + ' ' + chr(95) + '   ' + chr(95) + chr(41) + '\n'
        bottom_row = ' ' + chr(124) + chr(95) + chr(95) + chr(40) + ' ' + chr(41) + chr(95) + chr(124) + '\n'
        first_vertical_piece = top_row + middle_row + bottom_row
        return first_vertical_piece

    if width > 1 and height == 1:
        print(horizontal_tiles(), 'horizontal tiles')
        return horizontal_tiles()
    elif width == 1 and height > 1:
        full_puzzle = str(initial_tile()) + str(first_vertical_tile())
        # print(first_vertical_tile(), 'just the tile')
        print(full_puzzle, 'vertical tiles')
        return first_vertical_tile()
    elif width == 1 and height == 1:
        print('one tile')
        return initial_tile()
    else:
        full_puzzle = str(horizontal_tiles()) + str(first_vertical_tile())
        print(full_puzzle)
        return full_puzzle



puzzle_tiles(1,5)
#
# '   _( )__ _( )__ _( )__\n _|     _|     _|     _|\n(_   _ (_   _ (_   _ (_\n |__( )_| _( )_| _( )_|' should equal
# '   _( )__ _( )__ _( )__\n _|     _|     _|     _|\n(_   _ (_   _ (_   _ (_\n |__( )_|__( )_|__( )_|\n |_     |_     |_     |_\n  _) _   _) _   _) _   _)\n |__( )_|__( )_|__( )_|'
# '|_     |_\n _) _   _)\n|__( )_|\n' should equal
# '   _( )__ _( )__ _( )__\n _|     _|     _|     _|\n(_   _ (_   _ (_   _ (_\n |__( )_|__( )_|__( )_|\n |_     |_     |_     |_\n  _) _   _) _   _) _   _)\n |__( )_|__( )_|__( )_|'
