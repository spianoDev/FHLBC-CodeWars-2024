# Source https://www.codewars.com/kata/563a631f7cbbc236cf0000c2

# In this game, the hero moves from left to right.
# The player rolls the dice and moves the number of spaces indicated by the dice two times.
#
# Create a function for the terminal game that takes the current position of the hero
# and the roll (1-6) and return the new position.
#
# Example:
# move(3, 6) should equal 15

def move(position, roll):
    new_position = position + (roll * 2)
    print(f'Player has moved from {position} to {new_position}')
    return new_position

move(0, 4) # => 8
move(3, 6) # => 15
move(2, 5) # => 12
