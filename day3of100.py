# Source https://www.codewars.com/kata/568018a64f35f0c613000054/train/python

# Imagine you are creating a game where the user has to guess the correct number. But there is a limit of how many
# guesses the user can do.

# If the user tries to guess more than the limit, the function should throw an error.
# If the user guess is right it should return true.
# If the user guess is wrong it should return false and lose a life.
# Can you finish the game so all the rules are met?

# Original provided code:
# class Guesser:
#     def __init__(self, number, lives):
#         self.number = number
#         self.lives = lives
#
#     def guess(self,n):
#         return False
from random import randint


class Guesser:
    def __init__(self, num, lives):
        self.number = num
        self.lives = lives

    def guess(self,n):
        print(self.number, n)
        if self.lives <= 0:
            raise Exception('Omae wa mo shindeiru')
        elif self.number == n:
            print('true')
            return True
        elif self.number != n:
            self.lives -= 1
            print('false')
            return False



guesser = Guesser(10, 2)
# guesser.guess(10) # => True
guesser.guess(1) # => False
guesser.guess(2) # => ERROR
