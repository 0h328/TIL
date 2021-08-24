import sys
from pandas import DataFrame
sys.stdin = open('input.txt')


def dfs(row, col):
    visited[row][col] = 1

    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)

    for d in range(4):
        new_r = row + dr[d]
        new_c = col + dc[d]
        if 0 <= new_r < N and 0 <= new_c < N:
            if visited[new_r][new_c] == 0 and grid[new_r][new_c] != 1:
                dfs(new_r, new_c)


T = int(input())
tc = 1
while tc <= T:
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, list(input()))))
    # print(DataFrame(grid))

    visited = [[0 for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if grid[r][c] == 2:
                start_r = r
                start_c = c
            elif grid[r][c] == 3:
                end_r = r
                end_c = c

    dfs(start_r, start_c)
    # print(DataFrame(visited))

    print('#{0} {1}'.format(tc, visited[end_r][end_c]))
    break
    tc += 1
