def bfs(r, c):
    global ans
    queue = []
    queue.append((r, c))
    visited[r][c] = 1
    while queue:
        tmp = queue.pop(0)
        for i in range(4):
            nr, nc = tmp[0] + dr[i], tmp[1] + dc[i]
            if arr[nr][nc] == 3:
                visited[nr][nc] = visited[tmp[0]][tmp[1]] + 1
                return visited[nr][nc]
            if not arr[nr][nc] and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = visited[tmp[0]][tmp[1]] + 1
    return 0
import sys
sys.stdin = open('input.txt')


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [[1]*(N+2)] + [[1] + list(map(int, input())) + [1] for _ in range(N)] + [[1]*(N+2)]
    visited = [[0]*(N+2)] + [[0] * (N+2) for _ in range(N)] + [[0]*(N+2)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    ans = 0
    x = 0
    y = 0
    for r in range(N+2):
        for c in range(N+2):
            if arr[r][c] == 2:
                y, x = r, c

    ans = bfs(y, x) - 2
    if ans < 0:
        ans = 0

    print('#{} {}'.format(test_case, ans))




