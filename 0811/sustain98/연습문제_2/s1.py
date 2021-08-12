import sys
sys.stdin = open('input2.txt')

t = int(input())
for idx in range(1,t+1):
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    total = 0
    for i in range(n):
        for j in range(n):
            for d_idx in range(4):
                ni = i + dx[d_idx]
                nj = j + dy[d_idx]
                if -1 < ni < n and -1 < nj < n:
                    total += abs(l[i][j] - l[ni][nj])


    print('#{} {}'.format(idx, total))