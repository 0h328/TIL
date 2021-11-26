import sys
sys.stdin = open('input.txt')


def dfs(x, y):
    global result
    if maze[x][y] == 3:
        result = 1
        return

    visited.add((x, y))

    for dx, dy in move:
        nx, ny = x + dx, y+dy
        if (0 <= nx < N) and (0 <= ny < N) and maze[nx][ny] != 1 and (nx, ny) not in visited:
            dfs(nx, ny)


T = int(input())
for test in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    result = 0

    for i in range(N**2):
        r = i // N
        c = i % N
        if maze[r][c] == 2:
            break

    dfs(r, c)
    print('#{} {}'.format(test+1, result))
