import sys
sys.stdin = open('input.txt')
def dfs(r, c):
    global result
    if maze[r][c] == 3:
        result = 1
        return
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < 16 and 0 <= nc <16:
            if maze[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                dfs(nr, nc)

for tc in range(1, 11):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    result = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_row = i
                start_col = j
    dfs(start_row, start_col)
    print('#{} {}'.format(T,result))
