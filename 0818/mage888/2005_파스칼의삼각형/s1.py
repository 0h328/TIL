import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    pascal = [[0] * i for i in range(1, N+1)]

    for i in range(N):
        if pascal[0][0] == 0:
            pascal[i][i] = 1
        else:
            pascal[i][0] += 1
            pascal[i][i] += 1

    if N > 2:
        for n in range(2, N):
            for k in range(1, N-1):
                if n == k:
                    break
                pascal[n][k] = pascal[n-1][k-1] + pascal[n-1][k]

    print('#{}'.format(tc))
    for i in range(N):
        print(*pascal[i])

