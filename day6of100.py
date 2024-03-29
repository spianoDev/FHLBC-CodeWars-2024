# Jumping ahead because I was inspired to create this program after a suggestion on how to spend my evening on a
# snowy day in March

import random

weather_outside = ['rain', 'sunny', 'snow', 'partly cloudy', 'sleet', 'windy', ]

def which_activity(weather):
    cold_weather_activities = ['read a book', 'watch a movie', 'sleep in', 'snuggle with a cat']
    warm_weather_activities = ['go for a walk', 'ride a bike', 'swim in the lake', 'eat dinner outside']
    if weather == 'rain' or weather == 'snow':
        print('It is cold outside so ' + random.choice(cold_weather_activities))
        return random.choice(cold_weather_activities)
    elif weather == 'sunny' or weather == 'partly cloudy':
        print('It is a beautiful day, why not ' + random.choice(warm_weather_activities))
        return random.choice(warm_weather_activities)
    else:
        print('The weather is so unpredictable, might as well ' + random.choice(cold_weather_activities +
                                                                      warm_weather_activities))
        return random.choice(cold_weather_activities + warm_weather_activities)


which_activity(random.choice(weather_outside))

