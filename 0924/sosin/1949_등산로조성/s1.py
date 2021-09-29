import sys
sys.stdin = open('input.txt')

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, ck, cnt):
    global result
    for k in range(4):
        nr = r+dr[k]
        nc = c+dc[k]
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
            visited[nr][nc]=1
            if san[nr][nc] < san[r][c]:
                # for i in range(N):
                #     print(*visited[i])
                # print()
                dfs(nr, nc, ck, cnt+1)
            elif not ck and san[nr][nc]-K < san[r][c]:
                temp = san[nr][nc]
                san[nr][nc] = san[r][c] - 1
                # for i in range(N):
                #     print(*visited[i])
                # print()
                dfs(nr, nc, True, cnt+1)
                san[nr][nc] = temp
            visited[nr][nc]=0
    if result < cnt:
        result = cnt

for T in range(int(input())):
    N, K = map(int, input().split())
    san = [list(map(int, input().split())) for _ in range(N)]
    height = 0
    goals = []
    for i in range(N):
        for j in range(N):
            if san[i][j] > height:
                goals = [(i, j)]
                height = san[i][j]
            elif san[i][j] == height:
                goals.append((i, j))

    result = 0
    visited = [[0]*N for _ in range(N)]
    for r, c in goals:
        visited[r][c] = 1
        dfs(r, c, False, 1)
        visited[r][c] = 0

    print('#{} {}'.format((T+1), result))

#1 6
#2 3
#3 7
#4 4
#5 2
#6 12
#7 6
#8 7
#9 10
#10 19
