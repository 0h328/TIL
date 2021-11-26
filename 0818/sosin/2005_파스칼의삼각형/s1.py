import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    N = int(input())
    tri = [[1]*i for i in range(1, N+1)]
    for i in range(N):
        for j in range(i-1):
            tri[i][j+1] = tri[i-1][j] + tri[i-1][j+1]

    print('#{}'.format((T+1)))
    [print(*row) for row in tri]