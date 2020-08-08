import numpy as np

# Question 1
# 1. Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
# in a comma-separated sequence on a single line.
print('Number 1:')
for i in range(2000, 3201):
    if i % 5 != 0 and i % 7 == 0:
        print(i, end=',')

# Question 2
# 2. Write a Python program to accept the user's first and last name and then getting them
# printed in the the reverse order with a space between first name and last name.
print('Number 2:')
name = input('Enter your first and last name ')
word = name.split()
print(word[-1], word[-2])

# Question 3
# 3. Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r**3
print('Number 3:')
r = 12
pi = 22/7
volume = (4/3) * pi * r**3
print('Volume:', volume)






