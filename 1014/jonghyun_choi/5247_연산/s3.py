import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    q = deque()
    q.append((N, 0))
    visited = {}
    while q:
        next_val, cnt = q.popleft()
        if visited.get(next_val, 0):
            continue
        visited[next_val] = 1
        if next_val == M:
            print('#{} {}'.format(case + 1, cnt))
            break

        if 0 < next_val + 1 <= 1000000:
            q.append((next_val + 1, cnt + 1))
        if 0 < next_val - 1 <= 1000000:
            q.append((next_val - 1, cnt + 1))
        if 0 < next_val * 2 <= 1000000:
            q.append((next_val * 2, cnt + 1))
        if 0 < next_val - 10 <= 1000000:
            q.append((next_val - 10, cnt + 1))

