# Question 1.1
# 1.1 Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()

# myreduce function
def myreduce(func, lists):
    x = lists[0]
    for i in lists[1:]:
        x = func(x, i)
    return x


def add(x1, x2):
    return x1 + x2


ans = myreduce(add, [1, 2, 3, 4])
print(ans)

# Question 1.2
#1.2 Write a Python program to implement your own myfilter() function which works exactly
#like Python's built-in function filter()

# myfilter function
def myfilter(func, sequence):
    x = []
    for number in sequence:
        if func(number):
            x.append(number)
    return x


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


adults = filter(myFunc, [22, 13, 21])
print(adults)
print(myfilter(myFunc, [22, 13, 21]))

# Question 2
# Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
# [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
# list comprehensions
seq = [a * i for a in ['x', 'y', 'z'] for i in range(1, 5)]
print(seq)

seq1 = [a * i for i in range(1, 5) for a in ['x', 'y', 'z']]
print(seq1)

seq2 = [[i + a] for i in range(2, 5) for a in range(3)]
print(seq2)

seq3 = [[a + i for a in range(2, 6)]for i in range(4)]
print(seq3)

seq4 = [(b, a) for a in range(1, 4) for b in range(1, 4)]
print(seq4)
