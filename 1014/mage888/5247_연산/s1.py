from collections import deque

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    v = [0] * 1000001
    q = deque()
    q.append((N, 0))

    v[N] = 1
    while q:
        s, cnt = q.popleft()

        cal = [s+1, s-1, s*2, s-10]

        if s == M:
            break

        for i in cal:
            if 1 <= i <= 1000000 and not v[i]:
                q.append((i, cnt+1))
                v[i] = 1

    print('#{} {}'.format(tc, cnt))



