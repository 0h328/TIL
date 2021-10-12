import sys
sys.stdin = open('input.txt')

def find_sets(x, y):
    global res
    for c in range(n-x-1, 1, -1):
        for a in range(c-1,  0, -1):
            b = c-a
            s = {l[nx][ny]}
            nx, ny = a, b
            for _ in range(b):
                nx += dx[0]
                ny += dy[0]
                if l[nx][ny] in s:
                    break
                s.add(nx, ny)





t = int(input())
dx = [1, 1, -1, -1]#우하,좌하,좌상,우상
dy = [1, -1, -1, 1]
for idx in range(1, t+1):
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for i in range(n-1):
        for j in range(1, n-1):
            find_sets(i, j)

    print('#{} {}'.format(idx, res))
