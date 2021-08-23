import sys
sys.stdin = open('input.txt')

# 1. 허락 받고 구하자
T = int(input())

for t in range(1, T+1):
    word = [0] * 5

    max_len = 0

    for i in range(5):
        word[i] = list(input())
        if len(word[i]) > max_len:
            max_len = len(word[i])

    print('#{}'.format(t), end=' ')

    for i in range(max_len):
        for j in range(5):
            if len(word[j]) > i:
                print(word[j][i], end='')
    print()