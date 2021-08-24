import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # print(maze)
    # print(visited)

    start = 0
    end = 0
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 3:
                end = [r, c]
            elif maze[r][c] == 2:
                start = [r, c]

    # print(start, end)

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    k = 0

    while visited[nr][nc] == 1:
        nr = start[0] + dr[k]
        nc = start[1] + dc[k]

        if nr in range(N) and nc in range(N):
            if maze[nr][nc] == 0:
                start[0] = nr
                start[1] = nc
                visited[nr][nc] = 1

        k = (k + 1) % 4

    if start == end:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))





