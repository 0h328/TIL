import sys
sys.stdin = open('input.txt')
from collections import deque

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    h = [[10000] * N for _ in range(N)] # 1000이 최대인 줄 알고 1000 했을 때는 안 됐는데?!
    h[0][0] = 0
    q = deque()
    q.append((0, 0))
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                cost = 1
                if arr[ni][nj] > arr[i][j]:
                    cost += arr[ni][nj] - arr[i][j]
                if h[ni][nj] > h[i][j] + cost:
                    h[ni][nj] = h[i][j] + cost
                    q.append((ni, nj))
    ans = h[-1][-1]
    print('#{} {}'.format(t, ans))