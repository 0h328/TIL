import sys
sys.stdin = open('input.txt')

ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    m = (1 << N)
    DP = [1] + [0] * (m - 1)
    for i in range(m):
        t = bin(i).count('1')  # 다음 인덱스를 찾는 코드
        for j in range(N):
            if not (i & (1 << j)):  # 겹치지 않는 경우
                DP[i | (1 << j)] = max(DP[i | (1 << j)], A[t][j] / 100 * DP[i])  # 더 최댓값 저장

    ans.append('#{0} {1:.6f}'.format(tc, DP[-1] * 100))
print(*ans, sep='\n')
