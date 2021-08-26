def dfs(r, c):
    global ans
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if mazeArray[nr][nc] == 3:
            ans = 1
            return
        if not mazeArray[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc)

def bfs(r, c):
    global ans
    queue = []
    queue.append((r, c))
    while queue:
        tmp = queue.pop(0)
        if not visited[tmp[0]][tmp[1]]:
            visited[tmp[0]][tmp[1]] = 1
        for i in range(4):
            nr, nc = tmp[0] + dr[i], tmp[1] + dc[i]
            if mazeArray[nr][nc] == 3:
                ans = 1
                return
            if not mazeArray[nr][nc] and not visited[nr][nc]:
                queue.append((nr, nc))



import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    T = int(input())
    N = 16
    mazeArray = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    ans = 0
    x = 0
    y = 0
    for r in range(N):
        for c in range(N):
            if mazeArray[r][c] == 2:
                y, x = r, c
    # dfs(y, x)
    bfs(y, x)
    print('#{} {}'.format(test_case, ans))

