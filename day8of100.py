# Source https://www.codewars.com/kata/55e8beb4e8fc5b7697000036/train/python

# Create a move method for your hero to move through the level.
#
# Adjust the hero's position by changing the position attribute. The level is a grid with the following values:
#
# 00	01	02	03	04
# 10	11	12	13	14
# 20	21	22	23	24
# 30	31	32	33	34
# 40	41	42	43	44
# The dir argument will be a string
#
# up
# down
# left
# right
# If the position is not inside the level grid the method should throw an error and not move the hero

## This builds upon the class created in day 7, so I will be importing that file ##
from day7of100 import Hero

# def add_leading_zero(answer):
#     if len(answer) == 1:
#         return '0' + answer
#     else:
#         return answer
def add_leading_zero(answer):
    if len(answer) == 1:
        return '0' + answer
    else:
        return answer

def move(self, direction):
    if direction == 'up' and int(self.position) < 10:
        raise ValueError(f'Direction {direction} is out of bounds. Player remains on position {self.position}')
    elif direction == 'up' and int(self.position) >= 10:
        self.position = str(int(self.position) - 10)
        print(f'new position is {add_leading_zero(self.position)}')
        return add_leading_zero(self.position)
    if direction == 'down' and int(self.position) > 34:
        raise ValueError(f'Direction {direction} is out of bounds. Player remains on position {self.position}')
    elif direction == 'down' and int(self.position) < 44:
        self.position = str(int(self.position) + 10)
        print(f'new position is {add_leading_zero(self.position)}')
        return add_leading_zero(self.position)
    if direction == 'left' and int(self.position) % 10 == 0:
        raise ValueError(f'Direction {direction} is out of bounds. Player remains on position {self.position}')
    elif direction == 'left' and int(self.position) % 10 != 0:
        self.position = str(int(self.position) - 1)
        print(f'new position is {add_leading_zero(self.position)}')
        return add_leading_zero(self.position)
    if direction == 'right' and (int(self.position) + 1) % 5 == 0:
        raise ValueError(f'Direction {direction} is out of bounds. Player remains on position {self.position}')
    elif direction == 'right' and (int(self.position) + 1) % 5 != 0:
        self.position = str(int(self.position) + 1)
        print(f'new position is {add_leading_zero(self.position)}')
        return add_leading_zero(self.position)

Hero.move = move

myHero = Hero()
# print(myHero)
myHero.position = '11'
# myHero.move('up')
# myHero.move('down')
# myHero.move('right')
# myHero.move('up')
# myHero.move('left')
# test.assert_equals(myHero.position, '00')
# myHero.move('down')
# test.assert_equals(myHero.position, '10')
# myHero.move('right')
# test.assert_equals(myHero.position, '11')
myHero.move('up')
# test.assert_equals(myHero.position, '01')
myHero.move('right')
# test.assert_equals(myHero.position, '02')
