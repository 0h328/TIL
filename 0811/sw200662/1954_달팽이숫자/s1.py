import sys
sys.stdin = open('input.txt')

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for z in range(T):
    a = int(input())
    b = []
    c = []
    value = 0
    for _ in range(a):
        c = []
        for _ in range(a):
            c.append(value)
        b.append(c)
    cnt = 1
    i,j = 0,-1
    k = 0
    while cnt <= a*a:
        ni, nj = i+di[k], j+dj[k]
        if ni <= a-1 and nj <= a-1 and b[ni][nj] == 0:
            b[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            k = (k+1) % 4
            if ni <= a-i:
                ni -= 1
            else:
                nj -= 1
    print('#{}'.format(z+1))
    for width in range(a):
        for height in range(a):
            print(b[width][height], end=' ')
            if height == a-1:
                print()