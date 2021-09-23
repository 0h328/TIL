import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    ans = N * M

    colors = [[0] * 3 for _ in range(N)]

    for i in range(N):
        colors[i][0] = arr[i].count('B') + arr[i].count('R')
        colors[i][1] = arr[i].count('W') + arr[i].count('R')
        colors[i][2] = arr[i].count('W') + arr[i].count('B')

    w = 1
    while w < N-1:
        b = 1
        while b < N-w:
            temp = 0
            for i in range(w):
                temp += colors[i][0]
            for j in range(w, w+b):
                temp += colors[j][1]
            for k in range(w+b, N):
                temp += colors[k][2]
            if temp < ans:
                ans = temp
            b += 1
        w += 1

    print('#{} {}'.format(t, ans))