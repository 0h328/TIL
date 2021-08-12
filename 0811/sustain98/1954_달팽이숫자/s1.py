import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1,t+1):
    n = int(input())
    l = [[0]*n for _ in range(n)]
    tmp_x = [0, 1, 0, -1]
    tmp_y = [1, 0, -1, 0]

    val = 1
    x = 0
    y = 0
    i = 0
    while val <= n**2:
        l[x][y] = val
        val += 1
        nx = x + tmp_x[i]
        ny = y + tmp_y[i]
        if -1 < nx < n and -1 < ny < n and l[nx][ny] == 0:
            x = nx
            y = ny
            # print('edge:',x,y)
        else:
            i = (i+1) % 4
            x += tmp_x[i]
            y += tmp_y[i]
            # print('ok:', x, y)

    print('#{}\n{}'.format(idx,'\n'.join(map(lambda x :' '.join(map(str, x)), l))))
