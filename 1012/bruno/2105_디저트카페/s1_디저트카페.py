import sys
sys.stdin = open('input.txt')


def dfs(r, c, k, cnt):
    global max_cnt
    r = r + dr[k]
    c = c + dc[k]
    visited[r][c] = 1
    if r == sr and c == sc:
        if cnt > max_cnt:
            max_cnt = cnt
        return
    if r < 0 or r >= N or c < 0 or c >= N or visited[r][c]:
        return






T = int(input())
for t in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    print(cafe)
    # [[9, 8, 9, 8], [4, 6, 9, 4], [8, 7, 7, 8], [4, 5, 3, 5]]
    dr = [1, 1, -1, -1]     # 5시, 7시, 11시, 1시 방향
    dc = [1, -1, -1, 1]
    max_cnt = -1
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            sr, sc = r, c
            dfs(r, c, 0, 1)