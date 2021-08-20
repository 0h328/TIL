import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    arr = [[[0 for _ in range(7)] for _ in range(7)] for _ in range(4)]
    N = int(input())
    for i in range(N):
        arr[0][i] = list(map(int, input().split()))

    for k in range(1, 4):
        for i in range(N-1, -1, -1):
            for j in range(N):
                arr[k][j][N-1-i] = arr[k-1][i][j]

    print('#{}'.format(tc))
    for i in range(N):
        for k in range(1, 4):
            if k != 1: print(end=' ')
            for j in range(N):
                print(arr[k][i][j], end='')
        print()