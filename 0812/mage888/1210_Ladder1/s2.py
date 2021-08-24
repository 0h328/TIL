def search(start):

    r = 99  # 목적지는 무조건 99번째 행에 있으므로 고정
    c = start

    dr = [-1, 0, 0]  # r은 위로 갈때 -1, 좌,우로 갈때는 0
    dc = [0, 1, -1]  # c는 위로 갈때 0, 우로 갈때 1, 좌로 갈때 -1

    i = 0

    while r > 0:  # r이 0이 되면 출발지를 찾았으므로 종료
        nr = r + dr[i]  # nr은 r이 배열 내 dr만큼 이동한 곳
        nc = c + dc[i]  # nc는 c가 배열 내 dc만큼 이동한 곳

        if nr in range(100) and nc in range(100):  # 범위 벗어나는 것을 방지
            if l[nr][nc] == 1:
                r = nr
                c = nc
                l[nr][nc] = -1

        i = (i + 1) % 3

    return c

import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    n = int(input())
    l = [list(map(int,input().split())) for _ in range(100)]

    goal = 0
    for c in range(100):
        if l[99][c] == 2:
            goal = c

    ans = search(goal)

    print('#{} {}'.format(tc, ans))

