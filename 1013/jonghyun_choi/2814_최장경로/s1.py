import sys
sys.stdin = open('input.txt')


def dfs(start, cnt):
    global answer
    if answer < cnt:
        answer = cnt

    for i in range(N):
        if data[start][i] and visited[i] == 0:
            visited[i] = 1
            dfs(i, cnt + 1)
            visited[i] = 0

T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    data = [[0] * N for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        data[a - 1][b - 1] = 1
        data[b - 1][a - 1] = 1
    answer = 0
    visited = [0] * N
    for i in range(N):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0
    print('#{} {}'.format(case + 1, answer))