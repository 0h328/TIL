import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    Q = deque(list(map(int,input().split())))
    idx_que = deque(list(range(N)))
    cnt = 0

    while Q:

        if Q[0] == max(Q):
            cnt += 1
            Q.popleft()
            if idx_que.popleft() == M:
                print(cnt)
        else:
            Q.append(Q.popleft())
            idx_que.append(idx_que.popleft())