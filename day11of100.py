# Source https://www.codewars.com/kata/586c1cf4b98de0399300001d/train/python

# Create a combat function that takes the player's current health and the amount of damage received,
# and returns the player's new health. Health can't be less than 0.
from day7of100 import Hero

def combat(self, enemy, health, damage):
    if self.position == enemy.position:
        print(f'{self.name}, you see an enemy ahead! Prepare for COMBAT with {enemy.name}!!')
        if (health - damage) <= 0:
            self.health = health - damage
            print(f'{enemy.name} has struck a fatal blow! Your health is now {self.health} and you died...')
            return health
        else:
            self.health = health - damage
            print(f'Your remaining health is {self.health}')
            return health
    else:
        print(f'This location seems safe for now...')

# combat(100, 5) # => 95
# combat(83, 16) # => 67
# combat(20, 30) # => 0
