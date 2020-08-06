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
