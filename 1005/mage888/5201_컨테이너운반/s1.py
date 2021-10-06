from collections import deque

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 컨테이너 수, M: 트럭 수
    load = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)

    check, ans, i, j = 0, 0, 0, 0
    while True:
        if load[i] <= truck[j]:
            ans += load[i]
            i += 1
            j += 1
        else:
            i += 1
        check += 1
        if check == N or check == M:
            break

    print('#{} {}'.format(tc, ans))





