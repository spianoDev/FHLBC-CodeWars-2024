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

## I will return to this idea when all the other grasshopper pieces are done to stitch them together with 'real'
# functions ##
def typing(s):
    for letter in s:
        print(letter, end='', flush=True)
        sleep(.05)

def do_turn():
    def dice_roll():
        return randint(1, 6)
    def move():
        # placeholder function
        typing(f'Player moves to new position...\n')
    def combat():
        # placeholder function
        typing(f'Space is occupied... COMBAT!\n')
    def get_coins():
        return randint(10, 100)
    def buy_health():
        # placeholder function
        typing(f'Power up to restore health...\n')
    def print_status():
        # placeholder function
        typing(f'Player is now in position x with y health...\n')

    '''Run turn sequence'''
    typing(f'New turn: Player rolls {dice_roll()}\n')
    move()
    combat()
    typing(f'Congratulations warrior, you have won ${get_coins()}!!\n')
    buy_health()
    print_status()

do_turn()

## looks like this kata is asking for less creativity and more something else... ##

# def do_turn():
#     log = ['dice_roll', 'move', 'combat', 'get_coins', 'buy_health', 'print_status']
#     def dice_roll():
#         print('player rolled ')
#     def move():
#         print('Player moves to new position...')
#     def combat():
#         print('Space is occupied... COMBAT!')
#     def get_coins():
#         print('Collect coins')
#     def buy_health():
#         print('Power up to restore health...')
#     def print_status():
#         print('Player is now in position x with y health...')
#
#     '''Run turn sequence'''
#     dice_roll()
#     move()
#     combat()
#     get_coins()
#     buy_health()
#     print_status()
#
# do_turn()

## I don't understand what this one is asking for so I wrote a nifty little program ##
