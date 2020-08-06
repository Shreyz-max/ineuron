try:
    print(5/0)
except:
    print('Error dividing by zero')

subjects = ["Americans ", "Indians "]
verbs = ["play ", "watch "]
objects = ["Baseball", "Cricket"]

for subject in subjects:
    for verb in verbs:
        for object1 in objects:
            sentence = subject + verb + object1
            print(sentence)