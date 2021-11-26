import sys

sys.stdin = open('input.txt')


def check(str):
    cnt = 0
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            word = str[i:j]
            if word == word[::-1]:
                if len(word) == M:
                    cnt += 1
    return cnt


for test in range(10):
    M = int(input())

    data = [input() for _ in range(8)]
    trans = [''.join(i) for i in zip(*data)]
    answer = 0
    for i in data:
        answer += check(i)

    # trans = []
    # for i in range(8):
    #     string = ''
    #     for j in range(8):
    #         string += data[j][i]
    #     trans.append(string)

    for i in trans:
        answer += check(i)

    print('#{} {}'.format(test + 1, answer))
