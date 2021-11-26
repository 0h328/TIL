from pandas import DataFrame

# 0 길 / 1 벽 / 2 출발 / 3 도착

dx = [0, 1, 0, -1]      # 우하좌상
dy = [1, 0, -1, 0]

def dfs(x, y):
    global result           # result 함수 밖이라

    if maze[x][y] == 3:
        result = 1
        return              # 종료

    stack.append((x, y))    # 방문등록(보단 내가 밟았으니가 발자취를 남겼다?)

    for i in range(4):      # 우하좌상~!
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 16 and 0 <= ny < 16 and (nx, ny) not in stack and (maze[nx][ny] == 0 or maze[nx][ny] == 3):
            dfs(nx, ny)

import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())

    maze = [list(map(int, input())) for _ in range(16)]
    # print(maze)
    # print(DataFrame(maze))

    result = 0
    stack = []
    dfs(1, 1)
    print('#{} {}'.format(tc, result))