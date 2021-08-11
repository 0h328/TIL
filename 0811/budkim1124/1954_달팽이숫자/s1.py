import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(1, T+1):
    N = int(input())
    arr = [[0]*N] *N
    cnt = 1

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    i, j = 0, -1
    k = 0
    while cnt <= N * N:
        ni, nj = i + di[k], j + dj[k]
        if () and arr[ni][nj] == 0:
            arr[ni][nj] += cnt
            cnt += 1
            i, j = ni, nj
        else:
            k = (k + 1) % 4

    print("#{} {}".format(num, arr))