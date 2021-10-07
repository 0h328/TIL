import sys
sys.stdin = open('input.txt')


ans = []
T = int(input())
for tc in range(1, T + 1):
    N, *A = map(int, input().split())
    DP = [0] + [100] * len(A)

    for i in range(N-1):
        for j in range(A[i], 0, -1):
            if i + j < N:
                DP[i+j] = min(DP[i+j], DP[i]+1)

    ans.append('#{0} {1}'.format(tc, DP[N-1]-1))

print(*ans, sep='\n')
