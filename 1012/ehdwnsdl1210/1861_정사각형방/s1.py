# 18 / 27

import sys
sys.stdin = open('input.txt')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def Check_visited(x, y, n):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 > nx or nx >= N or 0 > ny or ny >= N or room[nx][ny] != n + 1:
            continue

        else:
            return

    visited[x][y] = 1


def DFS(x, y, n, c):
    global max_num

    if max_num < c:
        max_num = c

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if room[nx][ny] == n + 1:
                result.add(n)
                DFS(nx, ny, room[nx][ny], c + 1)
                break


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    # print(room)
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            Check_visited(i, j, room[i][j])

    result = set()

    max_num = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                DFS(i, j, room[i][j], 1)

    print('#{} {} {}'.format(tc, min(result), max_num))

'''
#1 6 8
#2 3 2
#3 149 2
#4 2 45
#5 2 23
#6 1 2
#7 1 4
#8 5 17
#9 4 2
#10 1 35
#11 2 2
#12 7 2
#13 45 2
#14 113 2
#15 12 32
#16 6 9
#17 1 4
#18 36 42
#19 204 2
#20 7 14
#21 4 2
#22 8225 2200
#23 35 3
#24 2 2
#25 613 2
#26 33 2
#27 5 5
'''