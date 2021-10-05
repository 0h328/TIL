import sys
sys.stdin = open('input.txt')


dr = [1, 0]
dc = [0, 1]

def dfs(r, c):
    global ans, res

    if res > ans:
        return

    if r == N - 1 and c == N - 1:
        if ans > res:
            ans = res
        return

    for k in range(2):
        next_r = r + dr[k]
        next_c = c + dc[k]
        if 0 <= next_r < N and 0 <= next_c < N and visited[next_r][next_c] == 0:
            visited[next_r][next_c] = 1
            res += road[next_r][next_c]
            dfs(next_r, next_c)
            res -= road[next_r][next_c]
            visited[next_r][next_c] = 0


T = int(input())

for case in range(T):
    N = int(input())
    road = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    ans = 987654321
    res = road[0][0]
    dfs(0, 0)
    print('#{} {}'.format(case + 1, ans))