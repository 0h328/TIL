import sys
sys.stdin = open('input2.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 상하좌우

    my_total = 0

    for i in range(N):
        if (-1 < nr < N) and (-1 < nc < N):




    while
        for i in range(4)
            nr = r + dr[i]
            nc = c + dc[i]

            total_sum += sum(abs(M[r][c] - M[nr][nc]))



#1 2430
#2 2244
#3 0