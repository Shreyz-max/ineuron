import numpy as np


print('Number 1:')
for i in range(2000, 3201):
    if i % 5 != 0 and i % 7 == 0:
        print(i, end=',')

print('Number 2:')
name = input('Enter your first and last name ')
word = name.split()
print(word[-1], word[-2])


print('Number 3:')
r = 12
pi = 22/7
volume = (4/3) * pi * r**3
print('Volume:', volume)






