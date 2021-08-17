import sys

sys.stdin = open('input.txt')

def check(str):
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            word = str[i:j]
            if word == word[::-1]:
                if len(word) == M:
                    return word


for test in range(int(input())):
    N, M = map(int, input().split())

    data = [input() for _ in range(N)]
    answer = ''

    for i in data:
        if check(i) != None:
            answer = check(i)
# 세로 전치행렬
    trans = []
    for i in range(N):
        string = ''
        for j in range(N):
            string += data[j][i]
        trans.append(string)

    for i in trans:
        if check(i) != None:
            answer = check(i)

    print('#{} {}'.format(test + 1, answer))
