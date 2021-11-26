import sys

sys.stdin = open('input.txt')

from collections import deque

for _ in range(10):
    N = int(input())
    data = list(map(int, input().split()))
    q = deque(data)
    i = 1
    while q:
        if i == 6:
            i = 1
        num = q.popleft()
        num -= i
        if num <= 0:
            q.append(0)
            break
        q.append(num)
        i += 1
    res = list(q)

    print('#{} {}'.format(N, ' '.join(map(str, res))))



