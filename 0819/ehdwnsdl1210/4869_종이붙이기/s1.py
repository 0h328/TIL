# dp
# 손으로

import sys
sys.stdin = open('input.txt')


def fold(n):
    f = [1, 3]
    for i in range(2, n+1):
        if i % 2 == 0:
            f.append(f[i-2] * 4 + 1)
        else:
            f.append(f[i-2] * 4 - 1)
    return f[n-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = N // 10
    print('#{} {}'.format(tc, fold(n)))