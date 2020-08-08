# Question 1.1
# 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

class Triangle:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def input_sides(self):
        self.a = int(input('a:'))
        self.b = int(input('b:'))
        self.c = int(input('c:'))


class Area(Triangle):
    def __init__(self):
        super().__init__()

    def get_area(self):
        a = self.a
        b = self.b
        c = self.c
        s = (a + b + c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return area


t = Area()
t.input_sides()
print(t.get_area())

# Question 1.2
# 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.

def filter_long_words(words, n):
    x = []
    for word in words:
        if len(word) > n:
            x.append(word)
    return x

# Question 2.1
# 2.1 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

seq = list(map(lambda x: len(x), ['ab', 'cde', 'erty']))
print(seq)

# Question 2.2
# 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
# it is a vowel, False otherwise.

def vowel_or_not(letter):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if letter in vowel:
        return True
    else:
        return False


print(vowel_or_not('u'))
