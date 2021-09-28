import sys
sys.stdin = open('input.txt')

def dfs(row, col, flag):
    global result
    if result < visited[row][col]:
        result = visited[row][col]
    for node in range(4):
        nr = dr[node] + row
        nc = dc[node] + col
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            if maps[nr][nc] < maps[row][col]:
                visited[nr][nc] = visited[row][col] + 1
                dfs(nr, nc, flag)
                visited[nr][nc] = 0
            elif flag and maps[nr][nc] - k < maps[row][col]:
                temp = maps[nr][nc]
                maps[nr][nc] = maps[row][col] - 1
                visited[nr][nc] = visited[row][col] + 1
                dfs(nr, nc, 0)
                visited[nr][nc] = 0
                maps[nr][nc] = temp


for tc in range(int(input())):
    n, k = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]                                            # 4가지 방향 설정
    flag = 1
    result = 0

    max_height = 0                                                # 가장 높은 등산로
    for x in range(n):
        for y in range(n):
            if maps[x][y] > max_height:
                max_height = maps[x][y]                           # 가장높은 등산로 높이를 구함
    # print(n, k, maps, max_height)
    results = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] == max_height:                          # 가장 높은 등산로의 경우에 dfs(start)
                visited[i][j] = 1
                dfs(i, j, flag)
                results.append(result)
    print(results)
