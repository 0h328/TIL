import sys
sys.stdin = open('input.txt')


# queue를 이용해 bfs로 탐색 시 Runtime Error 발생
from collections import deque

T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    q = deque()
    q.append((N, 0))
    while q:
        next_val, cnt = q.popleft()
        if next_val == M:
            print('#{} {}'.format(case + 1, cnt))
            break

        for k in range(4):
            if k == 0:
                q.append((next_val + 1, cnt + 1))
            elif k == 1:
                q.append((next_val - 1, cnt + 1))
            elif k == 2:
                q.append((next_val * 2, cnt + 1))
            elif k == 3:
                q.append((next_val - 10, cnt + 1))

