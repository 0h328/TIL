import sys
sys.stdin = open('input.txt')

T = int(input())

def blue(data,i,j):
    cnt = 0
    if data[i][j] != 'B':
        cnt += 1
    return cnt

def red(data,i,j):
    cnt = 0
    if data[i][j] != 'R':
        cnt += 1
    return cnt

def white(data,i,j):
    cnt = 0
    if data[i][j] != 'W':
        cnt += 1
    return cnt

def paint_count(data, s, e):
    cnt = 0
    for i in range(1, N-1):
        for j in range(M):
            if 0 < i < s:
                cnt += white(data, i ,j)
            elif e < i < N - 1:
                cnt += red(data, i, j)
            else:
                cnt += blue(data, i ,j)
    return cnt

for case in range(T):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]
    res = 0
    for i in range(M):
        if data[0][i] != 'W':
            res += 1
        if data[N-1][i] != 'R':
            res += 1

    min_val =987654321
    for i in range(1, N-1):
        for j in range(i, N-1):
            if min_val > paint_count(data, i, j):
                min_val = paint_count(data, i, j)


    res += min_val

    print('#{} {}'.format(case + 1, res))
