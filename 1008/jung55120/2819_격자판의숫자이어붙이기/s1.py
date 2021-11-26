# dfs에는 그냥 숫자를 들고 다니는게 맞는 것 같다.
# visited 쓰면서 놔두고 다녀봤자 소용 x임 -> 백트래킹 싫다 싫어!
# 뭐.. 결론은 해결 쁑 v^__^v

import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, my_str):
    global result
    if len(my_str) == 7:
        result.add(my_str)
        return

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, my_str + grid[nx][ny])



T = int(input())
for tc in range(1, T+1):
    grid = [list(input().split()) for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, grid[i][j])

    result = len(set(result))
    print('#{} {}'.format(tc, result))