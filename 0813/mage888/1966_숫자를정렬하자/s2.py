# 버블 정렬

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int,input().split()))


    for _ in range(len(a)-1, 0, -1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    print('#{}'.format(tc), end=' ')
    print(*a)