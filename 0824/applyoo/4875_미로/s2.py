import sys
sys.stdin = open('input.txt')


def bfs(x, y):
    bfs_list = deque([(x, y)])
    visited.add((x, y))

    while bfs_list:
        x, y = bfs_list.popleft()

        if maze[x][y] == 3:
            return 1
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if (0 <= nx < N) and (0 <= ny < N) and maze[nx][ny] != 1 and (nx, ny) not in visited:
                bfs_list.append((nx, ny))
                visited.add((nx, ny))
    return 0


from collections import deque

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

    print('#{} {}'.format(test+1, bfs(r, c)))
