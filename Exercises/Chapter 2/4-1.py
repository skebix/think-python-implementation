__author__ = 'skebix'

'''The volume of a sphere with radius r is 4/3 pi r3. What is the volume of a sphere with radius 5?
Hint: 392.7 is wrong!'''

pi = 3.14
radius = 5

volume = 4 / 3.0 * pi * radius ** 3 #Here we use 3.0, otherwise the floor division ruins our result

print volume