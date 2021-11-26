import sys

sys.stdin = open('input.txt')

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(cnt, x, y, s):
    global ans
    if cnt == 6:
        ans.append(s)
        return
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(cnt + 1, nx, ny, s + list_num[nx][ny])

for tc in range(1, T + 1):
    list_num = [list(input().split()) for _ in range(4)]
    ans = []
    for a in range(4):
        for b in range(4):
            dfs(0, a, b, list_num[a][b])
    ans = int(len(set(ans)))
    print('#{} {}'.format(tc, ans))
