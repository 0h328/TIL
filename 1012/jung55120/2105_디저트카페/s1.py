# 안풀린당,,, 너무 화가 난당,,,
# 나는 증말 바보다 으하하하하

import sys
sys.stdin = open('input.txt')

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
def dfs(x, y, way):
    global result
    if way == 4 and x == first_x and y == first_y:
        if len(visited) > result:
            result = len(visited)

    while way < 3:
        nx = dx[way] + x
        ny = dy[way] + y

        if 0 <= nx < N and 0 <= ny < N:
            if dessert[nx][ny] not in visited:
                visited.append(dessert[nx][ny])
                dfs(nx, ny, way)

        way += 1

        if visited:
            visited.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    for i in range(N):
        for j in range(N):
            visited = []
            first_x, first_y = i, j
            dfs(i, j, 0)

    print('#{} {}'.format(tc, result))