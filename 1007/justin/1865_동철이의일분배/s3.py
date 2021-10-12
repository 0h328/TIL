# dp
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = 1 << N                                           # 2^N
    dp = [[0.0 for _ in range(M)] for _ in range(N)]
    G = []
    for i in range(N):
        G.append(list(map(float, input().split())))
        for j in range(N):
            G[i][j] = G[i][j] / 100

    for i in range(N):
        dp[0][1 << i] = G[0][i]

    for i in range(1, N):
        for cur in range(1, M):
            if dp[i-1][cur] == 0:
                continue

            for j in range(N):
                if cur & (1 << j) != 0 or G[i][j] == 0:
                    continue
                next = cur | (1 << j)

                dp[i][next] = max(dp[i][next], dp[i-1][cur] * G[i][j])

    print('#{} {:.6f}'.format(tc, dp[N-1][M-1] * 100))