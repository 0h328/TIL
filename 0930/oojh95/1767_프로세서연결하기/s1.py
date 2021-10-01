import sys
sys.stdin = open('input.txt')

def work(r, c):
    tmp = [r, c]
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        while 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 1:
                break
            nr += dr[k]
            nc += dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            tmp.append(k)
    if len(tmp) >= 3:
        visited.append(tmp)


def draw_line(r, c, *arg):
    for l in range(len(arg)):
        nr = r + dr[arg[l]]
        nc = r + dc[arg[l]]
    while 0 <= nr < N and 0 <= nc < N and not arr[nr][nc]:
        arr[nr][nc] += 2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    for i in range(1, N-1):
        for j in range(1, N-1):
            if arr[i][j] == 1:
                work(i, j)
    visited = sorted(visited)
    for i in range(len(visited)):
        draw_line(visited[i][0], visited[i][1], visited[i][2:])
    print(visited)

