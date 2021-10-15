import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        p1, p2 = map(int, input().split())
        arr[p1].append(p2)
        arr[p2].append(p1)
    # print(arr)
    visited = [1] + [0] * N
    cnt = 0
    q = deque()

    for i in range(1, N+1):
        if visited[i] == 0:
            cnt += 1
            q.append(i)
            visited[i] = 1

        while q:
            idx = q.popleft()
            for j in arr[idx]:
                if not visited[j]:
                    q.append(j)
                    visited[j] = 1

    print('#{} {}'.format(t, cnt))