def check(str):
    my_max = []
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            word = str[i:j]
            if word == word[::-1]:
                my_max.append(len(word))

    return (my_max)


import sys

sys.stdin = open('input.txt')
for test in range(10):
    number = input()

    data = [input() for _ in range(100)]

    print(check(data[0]))
