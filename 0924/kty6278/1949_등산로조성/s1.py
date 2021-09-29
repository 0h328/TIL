import sys
from collections import deque
sys.stdin = open('input.txt')

def dfs(row, col, cnt, flag):
    global res
    if res < cnt + 1:
        res = cnt + 1
    visited[row][col] = 1
    for node in range(4):
        nr = dr[node] + row
        nc = dc[node] + col
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            if maps[nr][nc] < maps[row][col]:
                visited[nr][nc] = visited[row][col] + 1
                dfs(nr, nc, cnt+1, flag)
            elif flag and maps[nr][nc] - k < maps[row][col]:
                temp = maps[nr][nc]
                maps[nr][nc] = maps[row][col] - 1
                dfs(nr, nc, cnt+1, 0)
                maps[nr][nc] = temp
    visited[row][col] = 0

for tc in range(int(input())):
    n, k = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]                                            # 4가지 방향 설정
    flag = 1
    cnt = 0
    res = 0
    max_height = 0                                                # 가장 높은 등산로
    for x in range(n):
        for y in range(n):
            if maps[x][y] > max_height:
                max_height = maps[x][y]                           # 가장높은 등산로 높이를 구함
    # print(n, k, maps, max_height)
    print(maps)
    for i in range(n):
        for j in range(n):
            if maps[i][j] == max_height:                          # 가장 높은 등산로의 경우에 dfs(start)
                dfs(i, j, cnt, flag)
    print(res)
    print(visited)
