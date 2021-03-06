# Question 1
# 1. Create the below pattern using nested for loop in Python.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# without nested loops
a = 1
j = 1
k = 5
for i in range(2*k - 1):
    if j >= k:
        a = -1
    print('*' * j)
    j += a

# with nested loops
f = 1
for i in range(1, 2*k):
    if i <= k:
        for j in range(1, i+1):
            print('*', end='')
    else:
        for m in range(k, f, -1):
            print('*', end='')
        f += 1
    print('\r')

# Question 2
# 2. Write a Python program to reverse a word after accepting the input from the user.
# Input word: ineuron
# Output: norueni

word = input('Enter a word:')
print(word[::-1])
