# Source https://www.codewars.com/kata/586c1cf4b98de0399300001d/train/python

# Create a combat function that takes the player's current health and the amount of damage received,
# and returns the player's new health. Health can't be less than 0.

def combat(health, damage):
    if (health - damage) <= 0:
        print('You died!')
        return 0
    else:
        remaining_health = health - damage
        print(f'Your remaining health is {remaining_health}')
        return remaining_health

combat(100, 5) # => 95
combat(83, 16) # => 67
combat(20, 30) # => 0
