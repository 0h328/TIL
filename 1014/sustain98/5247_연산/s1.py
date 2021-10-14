import sys
sys.stdin = open('input.txt')
from collections import deque

t = int(input())
for idx in range(1, t+1):
    n, m = map(int, input().split())
    visited = [0] * 1000001
    q = deque([(n, 0)])
    while q:
        num, cnt = q.popleft()
        # visited[num] = 1 #여기서 하면 시간초과남
        if num == m:
            break
        if (num + 1) <= 1e6 and visited[num + 1] == 0:
            visited[num + 1] = 1
            q.append((num + 1, cnt + 1))
        if (num - 1) > 0 and visited[num - 1] == 0:
            visited[num - 1] = 1
            q.append((num - 1, cnt + 1))
        if (num * 2) <= 1e6 and visited[num * 2] == 0:
            visited[num * 2] = 1
            q.append((num * 2, cnt + 1))
        if (num - 10) > 0 and visited[num - 10] == 0:
            visited[num - 10] = 1
            q.append((num - 10, cnt + 1))

    print('#{} {}'.format(idx, cnt))
