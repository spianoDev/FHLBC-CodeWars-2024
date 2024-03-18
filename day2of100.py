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
    positive_response = {'words': 0, 'acts': 0, 'gifts': 0, 'time': 0, 'touch': 0}
    tries = weeks * 7
    loop_count = 0
    for n in range(tries):
        # Apparently having a loop inside will not pass so this is a much less efficient (and programmatically
        # annoying) solution
        if partner.response('words') == 'positive':
            positive_response['words'] += 1
        elif partner.response('acts') == 'positive':
            positive_response['acts'] += 1
        elif partner.response('gifts') == 'positive':
            positive_response['gifts'] += 1
        elif partner.response('time') == 'positive':
            positive_response['time'] += 1
        elif partner.response('touch') == 'positive':
            positive_response['touch'] += 1
        loop_count += 1
    print(positive_response, loop_count)
    likely_love_language = max(zip(positive_response.values(), positive_response.keys()))[1]
    print(likely_love_language)
    return likely_love_language

test_partner = TestPartner('words')
love_language(test_partner, 2)
test_partner2 = TestPartner('gifts')
love_language(test_partner2, 8)
