import sys
sys.stdin = open('input.txt')

ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    DP = [0] * (1 << N)
    DP[0] = 1
    for i in range((1 << N)):
        t = bin(i).count('1')
        for j in range(N):
            if not (i & (1 << j)) and A[t][j]:
                DP[i | (1 << j)] = max(DP[i | (1 << j)], A[t][j] / 100 * DP[i])

    ans.append('#{0} {1:.6f}'.format(tc, DP[-1] * 100))
print(*ans, sep='\n')