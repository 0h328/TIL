import sys

sys.stdin = open('input.txt')


def dfs(m, start):
    q = []
    q.append(start)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    m[start[0]][start[1]] = -1
    while q:
        xy = q.pop()
        x = xy[0]
        y = xy[1]
        for i in range(4):
            dxx = dx[i] + x
            dyy = dy[i] + y
            if m[dxx][dyy] == 3:
                return 1
            elif m[dxx][dyy] == 0:
                q.append((dxx, dyy))
                m[dxx][dyy] = -1
    return 0


for nn in range(10):
    test = int(input())
    m = []
    for i in range(16):
        m.append(list(input()))
    for x in range(16):
        for y in range(16):
            m[x][y] = int(m[x][y])
            if m[x][y] == 2:
                start = (x, y)
    ans = dfs(m, start)
    print("#%d %d" % (test, ans))
