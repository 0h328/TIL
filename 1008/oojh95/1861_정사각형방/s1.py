import sys
sys.stdin = open('input.txt')


def bfs(r, c):
    global result, first
    Q.append((r, c))
    visited[r][c] = 1
    while Q:
        r, c = Q.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] - 1 == arr[r][c] and not visited[nr][nc]:
                Q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
        if visited[r][c] > result:
            result = visited[r][c]
            first = arr[r][c] - visited[r][c] + 1
        elif visited[r][c] == result and arr[r][c] - visited[r][c] + 1 < first:
            first = arr[r][c] - visited[r][c] + 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    result = 0
    first = 1000000
    Q = []
    for i in range(N):
        for j in range(N):
            bfs(i, j)
            visited = [[0] * N for _ in range(N)]
    print('#{} {} {}'.format(tc, first, result))
