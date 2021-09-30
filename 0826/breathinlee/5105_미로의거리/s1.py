import sys
sys.stdin = open('input.txt')

def bfs(r, c):
    q = []
    q.append((r, c))
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if maze[nx][ny] == 3:
                    return visited[x][y]
                if maze[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                break

    print('#{} {}'.format(tc, bfs(r, c)))
