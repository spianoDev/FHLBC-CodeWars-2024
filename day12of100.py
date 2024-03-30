# Putting the Terminal Game Together as 2-person game: Computer Hero vs. spiano #

from day8of100 import * ## This is the move function ##
from day10of100 import * ## This is the turn sequence ##

# Day 7 Hero Class
class Hero(object):
    def __init__(self, name='Hero'):
        self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
        # print(self.name, self.position, self.health, self.damage, self.experience)

my_name = 'spiano'
computer_player = Hero()

player1 = Hero(my_name)



Hero.move = move
# print(myHero)
player1.position = '11'
computer_player.position = '44'
player1.move('up')
computer_player.move('left')
do_turn(player1)
