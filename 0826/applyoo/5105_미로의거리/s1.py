import sys
sys.stdin = open('input.txt')


def bfs(x, y):
    bfs_list = deque([(x, y)])
    visited = set([(x, y)])

    while bfs_list:
        x, y = bfs_list.popleft()

        if (x, y) == (end_x, end_y):
            return DP[x][y] - 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N):
                if arr[nx][ny] != 1 and (nx, ny) not in visited:
                    bfs_list.append((nx, ny))
                    visited.add((nx, ny))
                    DP[nx][ny] = DP[x][y] + 1
    return 0


from collections import deque

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
T = int(input())
for test in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    DP = [[0]*N for _ in range(N)]

    for i in range(N**2):
        r, c = divmod(i, N)
        if arr[r][c] == 2:
            start_x, start_y = r, c
        elif arr[r][c] == 3:
            end_x, end_y = r, c

    print('#{} {}'.format(test+1, bfs(start_x, start_y)))
