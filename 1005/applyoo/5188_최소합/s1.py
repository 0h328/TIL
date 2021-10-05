import sys
sys.stdin = open('input.txt')


ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    DP = [[300] * N for _ in range(N)]

    DP[0][0] = arr[0][0]
    for i in range(1, N):
        DP[0][i] = DP[0][i-1] + arr[0][i]

    for i in range(1, N):
        DP[i][0] = DP[i-1][0] + arr[i][0]

    for i in range(1, N):
        for j in range(1, N):
            DP[i][j] = min(DP[i-1][j] + arr[i][j], DP[i][j-1] + arr[i][j])

    ans.append('#{0} {1}'.format(tc, DP[N-1][N-1]))

print(*ans, sep='\n')
