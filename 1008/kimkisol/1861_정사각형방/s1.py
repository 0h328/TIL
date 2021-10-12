import sys

# 296ms
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt')
'''
방시작번호(여러개인 경우 가장 작은것), 최대 길이 출력
'''


def dfs(num, n_num, r, c, length):
    global max_len, start

    visited[n_num] = 1
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == n_num + 1:
            dfs(num, n_num + 1, nr, nc, length + 1)
            break
    else:
        if length > max_len:
            max_len = length
            start = num
        return


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [0] + [[0, 0] for _ in range(N * N)] # 행, 열 좌표
    visited = [0] * (N * N + 1)
    dr = [0, 1, 0, -1]  #우하좌상
    dc = [1, 0, -1, 0]
    max_len = 0
    start = 0

    # 1~N*N까지 좌표 작성
    for i in range(N):
        for j in range(N):
            p[arr[i][j]][0], p[arr[i][j]][1] = i, j

    for i in range(1, N * N + 1):
        if not visited[i]:
            dfs(i, i, p[i][0], p[i][1], 1)
    print(p)

    print('#{} {} {}'.format(t, start, max_len))