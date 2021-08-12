import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    n = int(input())
    l = [[0]*n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    val = 1
    x, y = 0, 0
    d_idx = 0
    while val <= n**2:
        l[x][y] = val
        val += 1
        nx = x + dx[d_idx]
        ny = y + dy[d_idx]
        if -1 < nx < n and -1 < ny < n and l[nx][ny] == 0:
            x = nx
            y = ny
        else:
            d_idx = (d_idx+1) % 4
            x += dx[d_idx]
            y += dy[d_idx]


    # print('#{}\n{}'.format(idx,'\n'.join(map(lambda x :' '.join(map(str, x)), l))))
    print('#{}'.format(idx))
    for sub_l in l:
        print(' '.join(map(str, sub_l)))
