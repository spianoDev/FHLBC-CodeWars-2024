# Source: https://www.codewars.com/kata/5aa7a581fd8c06b552000177/train/python

# You will be given a partner instance, and n weeks. The partner has a .response method, and the responses may be:
# "positive" or "neutral". You can try to get a response once a day, thus you have n * 7 tries in total to find the main love language of your partner!
#
# The love languages are: "words", "acts", "gifts", "time", "touch" (available predefined as LOVE_LANGUAGES)
#
# Note: your partner may (and will) sometimes give a positive response to any love language ("false positive"),
# but the main one has a much higher possibility. On the other hand, you may get a neutral response even for the main language,
# but with a low possibility ("false negative").
#
# There will be 50 tests. Although it's difficult to fail, in case you get unlucky, just run the tests again.
# After all, a few weeks may not be enough...
import random
LOVE_LANGUAGES = ["words", "acts", "gifts", "time", "touch"]
class TestPartner:
    def __init__(self, main_lang):
        self.main = main_lang
    def response(self, language):
        r = random.random()
        if language == self.main:
            if r < 0.85: return 'positive'
            else:        return 'neutral'
        else: # language != self.main
            if r < 0.15: return 'positive'
            else:        return 'neutral'

def love_language(partner, weeks):
    positive_response = []
    tries = weeks * 7
    for n in range(tries):
        for language in LOVE_LANGUAGES:
            if partner.response(language) == 'positive':
                positive_response.append(language)
                break
            else:
                pass

    def most_frequent(lst):
        return max(set(lst), key = lst.count)
    print(most_frequent(positive_response))
    return most_frequent(positive_response)


test_partner = TestPartner('words')
love_language(test_partner, 2)
test_partner2 = TestPartner('gifts')
love_language(test_partner2, 11)
