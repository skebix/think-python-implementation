__author__ = 'skebix'

'''
If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and
1 mile at easy pace again, what time do I get home for breakfast?
'''

start_time = (6 * 60 + 52) * 60 #In seconds

easy_pace_time = 2 * (8 * 60 + 15)

tempo_pace_time = 3 * (7 * 60 + 12)

total_time = start_time + easy_pace_time + tempo_pace_time

hour = total_time / 3600

minutes = (total_time - hour * 3600) / 60

print hour, minutes