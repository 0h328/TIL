import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    n = int(input())

    arr = [[0] * n for _ in range(n)] # 0으로 채워진 2차원 배열 만들기

    di = [0, 1, 0, -1] # 행 방향 조절
    dj = [1, 0, -1, 0] # 열 방향 조절

    i, j, k = 0, -1, 0
    num = 1

    while num <= n * n:
        ni = i + di[k]
        nj = j + dj[k]
        valid = 0 <= ni < n and 0 <= nj < n
        if valid and arr[ni][nj] == 0: # 구간 내, 아직 안 채워졌을 때
            arr[ni][nj] = num
            num += 1
            i, j = ni, nj
        else:
            k = (k+1) % 4

    print('#{}'.format(t))
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()