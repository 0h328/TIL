import sys
sys.stdin = open('input.txt')

def dfs(idx, min_x):
    global result
    if result < min_x:
        return
    if idx == N:
        result = min_x
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(idx + 1, min_x + N_list[i][idx])
            visited[i] = 0

tc = int(input())
for t in range(1, tc + 1):
    result = 1000000
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    dfs(0, 0)
    print("#{} {}".format(t, result))