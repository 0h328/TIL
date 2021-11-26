import sys
sys.stdin = open('input.txt')


def bfs(r, c):
    global result
    Q.append((r, c))
    while Q:
        a, b = Q.pop(0)
        for k in range(4):
            nr = a + dr[k]
            nc = b + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] > arr[a][b]:
                    tmp = visited[a][b] + 1 + arr[nr][nc] - arr[a][b]
                else:
                    tmp = visited[a][b] + 1
                if tmp < visited[nr][nc]:
                    visited[nr][nc] = tmp
                    Q.append((nr, nc))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    Q = []
    visited = [[100000000]*N for _ in range(N)]
    visited[0][0] = 0
    bfs(0, 0)
    print('#{} {}'.format(tc, visited[N-1][N-1]))