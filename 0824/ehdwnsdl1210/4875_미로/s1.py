# 재귀 or Stack
import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(x, y):
    global result   # 이걸?

    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]

    if arr[x][y] == 3:
        result = 1
        return  # 마무리를 위해? 함수정지를 위해!

    stack.append((x, y))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in stack and (arr[nx][ny] == 0 or arr[nx][ny] == 3):
            dfs(nx, ny)
            # stack.remove((nx, ny))

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    x, y = 0, 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j

    result = 0
    stack = []
    dfs(x, y)
    print('#{} {}'.format(tc, result))