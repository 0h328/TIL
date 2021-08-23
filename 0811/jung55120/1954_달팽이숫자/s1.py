import sys
sys.stdin = open('input.txt')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    cnt = 1
    N = int(input())
    arr = [[0] * N for i in range(N)]
    i, j = 0, -1
    k = 0
    while cnt <= N*N:
        ni, nj = i+di[k], j+dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            arr[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            k = (k+1) % 4

    print('#{}'.format(tc))
    for i in range(len(arr)):
        print(*arr[i])

    # for j in range(n):
    #     for k in range(n-1, -1, -1):
    #         if stack[j][k] == 0:
    #             stack[j].pop(k)
    #
    #     print(*stack[j])