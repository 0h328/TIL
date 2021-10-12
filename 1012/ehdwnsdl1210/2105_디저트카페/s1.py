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
                if n > 3 and (nr, nc) == original_idx:
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
            # delta_list = [0] * 4
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
'''