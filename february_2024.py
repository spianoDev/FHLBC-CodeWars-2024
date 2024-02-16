# Source: https://www.codewars.com/kata/57f24e6a18e9fad8eb000296/train/python
# Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:

# "I love you"
# "a little"
# "a lot"
# "passionately"
# "madly"
# "not at all"
# If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.

# When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

# Your goal in this kata is to determine which phrase the girls would say at the last petal for a flower of a given number of petals. The number of petals is always greater than 0.

def how_much_i_love_you(nb_petals):
  # Possible choices for each petal pull
  love_phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
  # Determining the location if the number is greater than 6 by using the remaining value of nb_petals divided by 6 and then subtracting 1 because lists begin with position 0
  phrase_location = (nb_petals % 6) - 1
  print(love_phrases[phrase_location])
  return love_phrases[phrase_location]

# test case
how_much_i_love_you(11) # => "madly"
