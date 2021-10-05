import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    temp = [(0, -1), (-1, 0)]

    for i in range(n):
        for j in range(n):
            val = []
            for x, y in temp:
                ni, nj = i + x, j + y
                if -1 < ni < n and -1 < nj < n:
                    val.append(l[ni][nj])
            if val:
                l[i][j] += min(val)
    print('#{} {}'.format(idx, l[n-1][n-1]))
