import sys
sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 0

    dfs(0, 1)

    print('#{} {:.6f}'.format(t, ans*100))