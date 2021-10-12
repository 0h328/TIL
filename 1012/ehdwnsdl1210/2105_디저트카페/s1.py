# 24 / 50

import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 1, -1]     # 우상 / 우하 / 좌하 / 좌상
dc = [1, 1, -1, -1]


def DFS(r, c, n, k):
    global max_cnt

    visited[r][c] = 1
    dessert_value.append(dessert[r][c])     # 값 넣음, 중복 확인

    if k > 3:       # 이건.... 아닌가
        if max_cnt > n:
            return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        delta_list.append(i)        # delta 꺾이는지 확인 위해

        if 0 <= nr < N and 0 <= nc < N:                     # 범위 내
            if not visited[nr][nc]:                         # 노 방문
                if dessert[nr][nc] not in dessert_value:    # 노 중복

                    if delta_list[-1] != delta_list[-2]:    # delta 꺾임
                        DFS(nr, nc, n + 1, k + 1)
                    else:
                        DFS(nr, nc, n + 1, k)

                    delta_list.pop()
                    dessert_value.pop()

                else:
                    delta_list.pop()

            else:
                if n > 3 and (nr, nc) == original_idx and k < 5:
                    if max_cnt < n:
                        max_cnt = n
                        return
                else:
                    delta_list.pop()
        else:
            delta_list.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = -1
    cnt = 1             # 방문 갯수

    for i in range(1, N-1):     # 젤위, 젤아래 볼 필요 X
        for j in range(N):
            delta_list = [0]    # 초반은 0이니까 넣었음
            K = 0               # 꺾임

            dessert_value = []

            visited = [[0] * N for _ in range(N)]

            original_idx = (i, j)
            DFS(i, j, cnt, K)

    print('#{} {}'.format(tc, max_cnt))



'''
import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 1, -1]     # 우상 / 우하 / 좌하 / 좌상
dc = [1, 1, -1, -1]


def DFS(r, c, n):
    global max_cnt

    visited[r][c] = 1
    dessert_value.append(dessert[r][c])

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc]:
                if dessert[nr][nc] not in dessert_value:

                    DFS(nr, nc, n+1)
                    dessert_value.pop()

            else:
                if n > 3 and (nr, nc) == original_idx and i == 3:
                    if max_cnt < n:
                        max_cnt = n
                        return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = -1
    cnt = 1

    for i in range(1, N-1):
        for j in range(N):

            dessert_value = []

            visited = [[0] * N for _ in range(N)]

            original_idx = (i, j)
            DFS(i, j, cnt)

    print('#{} {}'.format(tc, max_cnt))
'''

#1 6
#2 -1
#3 4
#4 4
#5 8
#6 6
#7 14
#8 12
#9 18
#10 30
