import sys

# 279ms
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt')
'''
방시작번호(여러개인 경우 가장 작은것), 최대 길이 출력
'''


def dfs(num, n_num, r, c):
    global max_len, start

    visited[n_num] = 1
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == n_num + 1:
            dfs(num, n_num + 1, nr, nc)
            break
    else:
        length = n_num - num + 1
        if length > max_len:
            max_len = length
            start = num
        elif length == max_len and start > num:
            start = num
        return


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)
    dr = [0, 1, 0, -1]  # 우하좌상
    dc = [1, 0, -1, 0]
    max_len = 0
    start = N * N  # 시작 지점

    # 1~N*N까지 좌표 작성
    for i in range(N):
        for j in range(N):
            num = arr[i][j]
            if not visited[num]:
                dfs(num, num, i, j)

    print('#{} {} {}'.format(t, start, max_len))
