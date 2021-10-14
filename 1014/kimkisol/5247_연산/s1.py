import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100000)
'''
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.
단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.
'''

def dfs(N):

    if DP[N]:
        return DP[N]

    if N == M:
        return 0

    DP[N] = 1000000
    if 0 < N * 2 < 1000000:
        DP[N] = min(DP[N], dfs(N * 2) + 1)
    if 0 < N + 1 < 1000000:
        DP[N] = min(DP[N], dfs(N + 1) + 1)
    if 0 < N - 10 < 1000000:
        DP[N] = min(DP[N], dfs(N - 10) + 1)
    if 0 < N - 1 < 1000000:
        DP[N] = min(DP[N], dfs(N - 1) + 1)

    return DP[N]


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())  # N: 주어진 자연수, M: 만들어야 하는 자연수
    DP = [0] * 1000000

    print('#{} {}'.format(t, dfs(N)))