import sys

sys.stdin = open('input.txt')

T = int(input())


def find(start):
    global ans,depth
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    if ans < check[start[0]][start[1]]:
        ans = check[start[0]][start[1]]
    for k in range(4):
        new_x = start[0] + dx[k]
        new_y = start[1] + dy[k]
        if 0 <= new_x < N and 0 <= new_y < N and check[new_x][new_y] == 0:
            if mountain[start[0]][start[1]] > mountain[new_x][new_y]:
                check[new_x][new_y] = check[start[0]][start[1]] + 1
                find([new_x, new_y])
                check[new_x][new_y] = 0

            elif mountain[new_x][new_y] - mountain[start[0]][start[1]] < K and depth == 1:
                temp = mountain[new_x][new_y]
                mountain[new_x][new_y] = mountain[start[0]][start[1]] - 1
                check[new_x][new_y] = check[start[0]][start[1]] + 1
                depth = 0
                find([new_x, new_y])
                check[new_x][new_y] = 0
                depth = 1
                mountain[new_x][new_y] = temp

for tc in range(T):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for i in range(N)]
    depth = 1
    ans = 0

    max_height = 0
    for a in range(N):
        for b in range(N):
            if max_height < mountain[a][b]:
                max_height = mountain[a][b]
    max_axis = []
    for a in range(N):
        for b in range(N):
            if max_height == mountain[a][b]:
                max_axis.append([a, b])
    for z in max_axis:
        check = [[0] * N for _ in range(N)] # < 초기화 여기서하는거 매우 중요...
        check[z[0]][z[1]] = 1
        find(z)
    print('#{} {}'.format((tc+1),ans))
