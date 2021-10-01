import sys
sys.stdin = open('input.txt')


def dfs(x, y):
    global result
    for k in range(4):
        nx = x + dr[k]
        ny = y + dc[k]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if map_height[nx][ny] < map_height[x][y]:
                visited[nx][ny] = 1
                result += 1
                dfs(nx, ny)
                visited[nx][ny] = 0
                result -= 1
            elif cut and map_height[nx][ny] - K < map_height[x][y]:
                height_save = map_height[nx][ny]
                map_height[nx][ny] = map_height[x][y] - 1
                visited[nx][ny] = 1
                result += 1
                dfs(nx, ny)
                cut = False
                map_height[nx][ny] = height_save
                visited[nx][ny] = 0
                result -= 1

    return result


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N : 지도 한 변의 길이 / K : 최대 공사 가능 깊이
    map_height = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    peak = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    result = 0

    for i in range(N):
        for j in range(N):
            if map_height[i][j] == max(map_height[i]):
                peak.append([i, j])

    for p in peak:
        x, y = p[0], p[1]
        visited[x][y] = 1
        cut = False
        peak_len = []
        peak_len.append(dfs(x, y))

    print('#{} {}'.format(tc, max(peak_len)))