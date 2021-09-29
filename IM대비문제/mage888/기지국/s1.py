import sys
sys.stdin = open('input.txt')

from pandas import DataFrame

# 1. 지도를 순회한다.
# 2. 지도를 순회하다가 기지국을 만나면
#   2-2) 기지국의 유형을 판단한다. (A, B, C)
#   2-3) 기지국의 유형에 따라 커버할 범위를 정한다.
#   2-4) 정해진 범위만큼 커버 시작 (반복문 + 델타)
#       2-4-2) 단, 집이 아닐 경우는 무시한다.

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    data = [input() for _ in range(n)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    acoor = []  # A의 좌표 저장
    bcoor = []  # B의 좌표 저장
    ccoor = []  # C의 좌표 저장

    arr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if data[i][j] == 'H':
                arr[i][j] = 99
            elif data[i][j] == 'A':
                arr[i][j] = 1
                acoor.append((i, j))
            elif data[i][j] == 'B':
                arr[i][j] = 2
                bcoor.append((i, j))
            elif data[i][j] == 'C':
                arr[i][j] = 3
                ccoor.append((i, j))

    for k in range(4):
        if len(acoor):
            for l in range(len(acoor)):
                for m in range(1, 2):
                    nr = acoor[l][0] + dr[k]*m
                    nc = acoor[l][1] + dc[k]*m
                    if 0 <= nr < 9 and 0 <= nc < 9:
                        arr[nr][nc] = 1

        if len(bcoor):
            for l in range(len(bcoor)):
                for m in range(1, 3):
                    nr = bcoor[l][0] + dr[k]*m
                    nc = bcoor[l][1] + dc[k]*m
                    if 0 <= nr < 9 and 0 <= nc < 9:
                        arr[nr][nc] = 2

        if len(ccoor):
            for l in range(len(ccoor)):
                for m in range(1, 4):
                    nr = ccoor[l][0] + dr[k]*m
                    nc = ccoor[l][1] + dc[k]*m
                    if 0 <= nr < 9 and 0 <= nc < 9:
                        arr[nr][nc] = 3

    cnt = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 99:
                cnt += 1

    print('#{} {}'.format(tc, cnt))
