import sys

sys.stdin = open('input.txt')


def bfs(r, c):
    global result
    Q.append((r, c))
    visited.append((r, c))

    while Q:
        r, c = Q.pop(0)
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc <N:
                if maze[nr][nc] != 1 and (nr, nc) not in visited:
                    Q.append((nr, nc))
                    visited.append((nr, nc))
                    Distance[nr][nc] = Distance[r][c] + 1
                    if maze[nr][nc] == 3:
                        result = Distance[r][c]
                        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    Distance = [[0]*N for _ in range(N)]
    Q = []
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    result = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_row = i
                start_col = j

    bfs(start_row, start_col)
    print(visited)
    print(Distance)

    print('#{} {}'.format(tc, result))