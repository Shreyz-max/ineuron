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


def filter_long_words(words, n):
    x = []
    for word in words:
        if len(word) > n:
            x.append(word)
    return x


seq = list(map(lambda x: len(x), ['ab', 'cde', 'erty']))
print(seq)


def vowel_or_not(letter):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if letter in vowel:
        return True
    else:
        return False


print(vowel_or_not('u'))
