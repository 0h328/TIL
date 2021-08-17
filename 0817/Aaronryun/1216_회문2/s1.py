import sys

sys.stdin = open('input.txt')


def check(str):
    my_max = []
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            word = str[i:j]
            if word == word[::-1]:
                my_max.append(len(word))

    return (max(my_max))


for test in range(10):

    number = input()

    data = [input() for _ in range(100)]

    str_max = []
    for i in data:
        str_max.append(check(i))

    trans = []
    for i in range(100):
        string = ''
        for j in range(100):
            string += data[j][i]
        trans.append(string)

    str_max_col = []
    for i in trans:
        str_max_col.append(check(i))

    answer = [max(str_max), max(str_max_col)]

    print('#{} {}'.format(number, max(answer)))
