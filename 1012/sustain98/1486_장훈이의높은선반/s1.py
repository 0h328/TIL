import sys
sys.stdin = open('input.txt')
from collections import deque

t = int(input())
for idx in range(1, 1 + t):
    n, b = map(int, input().split())
    h = list(map(int, input().split()))
    res = 1e19
    q = deque([(0, -b)])
    while q:
        i, acc = q.popleft()
        if res > acc:
            if acc >= 0:
                res = acc
            elif i < n:
                q.append((i+1, acc + h[i]))
                q.append((i+1, acc))

    print('#{} {}'.format(idx, res))