# Jumping ahead because I was inspired to create this program after a suggestion on how to spend my evening on a
# snowy day in March

import random

def which_activity(weather):
    cold_weather_activities = ['read a book', 'watch a movie', 'sleep in', 'snuggle with a cat']
    warm_weather_activities = ['go for a walk', 'ride a bike', 'swim in the lake', 'eat dinner outside']
    if weather == 'rain' or weather == 'snow':
        print(random.choice(cold_weather_activities))
        return random.choice(cold_weather_activities)
    elif weather == 'sunny' or weather == 'partly cloudy':
        print(random.choice(warm_weather_activities))
        return random.choice(warm_weather_activities)

which_activity('snow')
which_activity('sunny')
