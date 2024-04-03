# Source https://www.codewars.com/kata/56019d3b2c39ccde76000086/train/python

# You are creating a text-based terminal version of your favorite board game.
# In the board game, each turn has six steps that must happen in this order:
# roll the dice, move, combat, get coins, buy more health, and print status.
#
# You are using a library (Game.Logic in C#) that already has the functions below.
# Create a function named doTurn/DoTurn/do_turn that calls the functions in the proper order
# as described in the paragraph above.
#
# - `combat`
# - `buy_health`
# - `get_coins`
# - `print_status`
# - `roll_dice`
# - `move`
from random import randint
from time import sleep
from day11of100 import * ## Pull in the combat function ##
from day8of100 import * ## Pull in the move function ##
from day13of100 import * ## Pull in buy health function ##

## I will return to this idea when all the other grasshopper pieces are done to stitch them together with 'real'
# functions ##
dice_roll = randint(1, 6)
move_options = ['blank', 'right', 'left', 'up', 'down', 'left', 'right']
def typing(s):
    for letter in s:
        print(letter, end='', flush=True)
        sleep(.05)

def do_turn(player, opponent):

    def get_coins():
        coin_win = randint(10, 100)
        player.money += coin_win
        typing(f'Congratulations warrior, you have won ${coin_win} and now carry {player.money}!!\n')

    def print_status(person):
        # print(person.name, person.position, person.health, person.damage, person.experience, person.money)
        typing(f'{person.name} is now in position {person.position} with {person.health} health and '
               f'{person.money} coins...\n')

    '''Run turn sequence'''
    typing(f'New turn: {player.name} rolls {dice_roll}\n')
    typing(f'{player.name} moves to new position...\n')
    typing('. . . . . . . . \n')
    # player.move(move_options[dice_roll])
    player.move(move_options[dice_roll])
    combat(player, opponent, player.health, opponent.damage)
    get_coins()
    buy_health(player, player.health, player.money)
    print_status(player)


