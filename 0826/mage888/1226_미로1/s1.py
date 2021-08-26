import sys
sys.stdin = open('input.txt')

def dfs(r, c):
    global ans

    rc = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for dr, dc in rc:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < 16 and 0 <= nc < 16 and not visited[nr][nc] and data[nr][nc] == '0':
            visited[nr][nc] = 1
            dfs(nr, nc)
        elif 0 <= nr < 16 and 0 <= nc < 16 and data[nr][nc] == '3':
            ans = 1
            return

for _ in range(1, 11):
    tc = int(input())
    data = [input() for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    ans = 0
    dfs(1, 1)

    print('#{} {}'.format(tc, ans))
