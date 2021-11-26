import sys
sys.stdin = open('input.txt')
from pandas import DataFrame
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    point = 0
    for r in range(1, N - 1):
        for c in range(1, N - 1):
            if arr[r][c] == 1:
                point += 1

    while point > 0:
        for r in range(1, N-1):
            for c in range(1, N-1):
                if arr[r][c] == 1:
                    cores.append([r, c])

        less = []
        for core in cores:
            cnt = 0
            r = core[0]
            c = core[1]
            direction = []
            for i in range(4):
                while True:
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] != 0:
                            cnt = 0
                            r = core[0]
                            c = core[1]
                            break
                        else:
                            r = nr
                            c = nc
                            cnt += 1
                    else:
                        r = core[0]
                        c = core[1]
                        break
                direction.append(cnt)
                cnt = 0
            less.append(direction)

        b = []
        for a in less:
            b.append(a.count(0))
        e = b.index(max(b))
        s = N-1
        for i in range(4):
            if less[e][i] != 0:
                if less[e][i] < s:
                    s = less[e][i]
        d = less[e].index(s)
        p = cores[e][0]
        q = cores[e][1]
        if d == 0:
            for c in range(q+1, N):
                arr[p][c] = 2
        elif d == 1:
            for r in range(p+1, N):
                arr[r][q] = 2
        elif d == 2:
            for c in range(q-1, -1, -1):
                arr[p][c] = 2
        else:
            for r in range(p-1, -1, -1):
                arr[r][q] = 2
        arr[cores[e][0]][cores[e][1]] = 3
        cores = []
        point -= 1

    # print(DataFrame(arr))
    ans = sum(arr, []).count(2)
    print('#{} {}'.format(test_case, ans))


