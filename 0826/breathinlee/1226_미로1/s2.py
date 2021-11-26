import sys
sys.stdin = open('input.txt')

def bfs(i, j):
    q = []
    q.append([i, j])
    while q:
        ri, rj = q.pop(0)
        for k in range(4):
            nr = ri + dr[k]
            nc = rj + dc[k]
            if 0 <= nr < 16 and 0 <= nc < 16:
                if maze[nr][nc] == 3:
                    return 1
                if maze[nr][nc] != 1 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append([nr, nc])
    return 0


for _ in range(10):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    # 1: 벽 / 2: 출발점 / 3: 도착점
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                i, j = r, c
                visited[i][j] = 1
                break


    print('#{} {}'.format(N, bfs(i, j)))