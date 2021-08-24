import sys
sys.stdin = open('input.txt')


def maze_visit(col, row):
    global result
    for i in range(4):
        ncol = col + dcol[i]
        nrow = row + drow[i]
        if 0 <= ncol < N and 0 <= nrow < N and visited[ncol][nrow] == 0:
            if maze[ncol][nrow] == 3:
                result = 1
                return
            if maze[ncol][nrow] == 0:
                visited[ncol][nrow] = 1
                maze_visit(ncol, nrow)


for tc in range(int(input())):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    dcol = [-1, 0, 0, 1]
    drow = [0, 1, -1, 0]
    result = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[j][i] == 2:
                row = i
                col = j
                break

    maze_visit(col, row)
    print(result)