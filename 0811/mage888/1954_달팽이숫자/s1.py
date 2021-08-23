import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    cnt = 1
    r, c = 0, -1
    i = 0

    while cnt <= N*N:
        nr, nc = r + dr[i], c + dc[i]
        if nr in range(N) and nc in range(N) and arr[nr][nc] == 0:
            arr[nr][nc] = cnt
            cnt += 1
            r, c = nr, nc
        else:
            i = (i+1) % 4

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
