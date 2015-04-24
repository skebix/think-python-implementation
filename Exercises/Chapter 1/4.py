__author__ = 'skebix'

'''If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile?
What is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).'''

miles = 10 / 1.61

seconds = 43 * 60 + 30

time_per_mile = seconds / miles

speed_mph = 3600 / time_per_mile

print miles, seconds, time_per_mile, speed_mph

