import sys
sys.stdin = open('input.txt')


def bfs(v):
    visited[v[0]][v[1]] = 1
    q.append(v)

    while q:
        v = q.pop()
        for d in range(4):
            new_r = v[0] + dr[d]
            new_c = v[1] + dc[d]
            if 0 <= new_r < grid_size and 0 <= new_c < grid_size:
                w = (new_r, new_c)

                if w[0] == end_r and w[1] == end_c:
                    return 1

                if grid[w[0]][w[1]] == 0 and not visited[w[0]][w[1]]:
                    visited[w[0]][w[1]] = 1
                    q.append(w)

    return 0


grid_size = 16
T = 10
tc = 1
while tc <= T:
    input()
    grid = []
    for _ in range(grid_size):
        grid.append(list(map(int, input())))

    visited = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    q = list()

    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)

    for r in range(grid_size):
        for c in range(grid_size):
            if grid[r][c] == 2:
                start_r = r
                start_c = c
            if grid[r][c] == 3:
                end_r = r
                end_c = c

    start = (start_r, start_c)
    ans = bfs(start)
    print('#{0} {1}'.format(tc, ans))
    # break
    tc += 1
