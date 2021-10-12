# bfs
from collections import deque
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = 1 << N
    dp = [[0.0 for _ in range(M)] for _ in range(N)]

    G = []
    for i in range(N):
        G.append(list(map(lambda x: float(x) / 100, input().split())))

    Q = deque()
    for i in range(N):
        Q.append((1, 1 << i, G[0][i]))

    ans = 0.0
    while len(Q) > 0:
        (k, cur, val) = Q.popleft()
        if cur == 0 or dp[k-1][cur] > val:
            continue
        if k == N:
            ans = max(ans, val)
        else:
            for i in range(N):
                if cur & (1 << i) != 0 or G[k][i] == 0:
                    continue
                next = cur | (1 << i)
                next_val = val * G[k][i]
                if dp[k][next] < next_val:
                    dp[k][next] = next_val
                    Q.append((k + 1, next, next_val))
    print('#{} {:.6f}'.format(tc, ans * 100))
