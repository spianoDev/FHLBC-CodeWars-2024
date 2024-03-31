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
from time import sleep

def add_leading_zero(answer):
    if len(answer) == 1:
        return '0' + answer
    else:
        return answer

def move(self, direction):
    if direction == 'up' and int(self.position) < 10:
        print(f'Direction {direction} is out of bounds. {self.name} remains on position {self.position}')
        return
    elif direction == 'up' and int(self.position) >= 10:
        self.position = add_leading_zero(str(int(self.position) - 10))
        print(f'{self.name}\'s new position is {add_leading_zero(self.position)}')
        return add_leading_zero(self.position)
    if direction == 'down' and int(self.position) > 34:
        print(f'Direction {direction} is out of bounds. {self.name} remains on position {self.position}')
        return
    elif direction == 'down' and int(self.position) < 44:
        self.position = add_leading_zero(str(int(self.position) + 10))
        print(f'{self.name}\'s new position is {add_leading_zero(self.position)}')
        return add_leading_zero(self.position)
    if direction == 'left' and int(self.position) % 10 == 0:
        print(f'Direction {direction} is out of bounds. {self.name} remains on position {self.position}')
        return
    elif direction == 'left' and int(self.position) % 10 != 0:
        self.position = add_leading_zero(str(int(self.position) - 1))
        print(f'{self.name}\'s new position is {add_leading_zero(self.position)}')
        return add_leading_zero(self.position)
    if direction == 'right' and (int(self.position) + 1) % 5 == 0:
        print(f'Direction {direction} is out of bounds. {self.name} remains on position {self.position}')
        return
    elif direction == 'right' and (int(self.position) + 1) % 5 != 0:
        self.position = add_leading_zero(str(int(self.position) + 1))
        print(f'{self.name}\'s new position is {add_leading_zero(self.position)}')
        return add_leading_zero(self.position)
    else:
        raise ValueError(f'Direction is not valid. {self.name} remains on position {self.position}')

Hero.move = move

# myHero = Hero()
# print(myHero)
# myHero.position = '11'
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
# myHero.move('up')
# test.assert_equals(myHero.position, '01')
# myHero.move('right')
# test.assert_equals(myHero.position, '02')
