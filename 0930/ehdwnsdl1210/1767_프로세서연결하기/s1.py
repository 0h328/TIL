'''
가로 N개 x 세로 N개의 cell
1개의 cell에는 1개의 Core 혹은 1개의 전선이 올 수 있다.
멕시노스의 가장 자리에는 전원이 흐르고 있다.

Core와 전원을 연결하는 전선은 직선으로만 설치가 가능하며,
전선은 절대로 교차해서는 안 된다.

최대한 많은 Core에 전원을 연결하였을 경우, 전선 길이의 합을 구하고자 한다.

단, 여러 방법이 있을 경우, 전선 길이의 합이 최소가 되는 값을 구하라!

1. 7 ≤  N ≤ 12
2. Core의 개수는 최소 1개 이상 12개 이하이다.
3. 최대한 많은 Core에 전원을 연결해도, 전원이 연결되지 않는 Core가 존재할 수 있다.

0은 빈 cell을 의미하며, 1은 core를 의미하고, 그 외의 숫자는 주어지지 않는다.
'''

# from pandas import DataFrame

def dfs(x, y, cnt):
    global wire_sum

    if x == 0 or x == N-1 or y == 0 or y == N-1:
        wire_sum += cnt
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and cell[nx][ny] == 0:
            dfs(nx, ny, cnt+1)



import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [-1, 0, 1, 0]      # 상 좌 하 우
dy = [0, -1, 0, 1]

for tc in range(1, T + 1):
    N = int(input())
    cell = [list(map(int, input().split())) for _ in range(N)]
    # print(DataFrame(cell))
    wire_sum = 0

    for i in range(N):      # 테두리는 다른걸로 지정해서 무시해주자!(어차피 연결이니까)
        if cell[0][i] == 1:
            cell[0][i] = 3
        elif cell[N - 1][i] == 1:
            cell[N - 1][i] = 3

    for i in range(1, N - 1):
        if cell[i][0] == 1:
            cell[i][0] = 3
        elif cell[i][N - 1] == 1:
            cell[i][N - 1] = 3
    # print(DataFrame(cell))

    for i in range(1, N-1):
        for j in range(1, N-1):
            if cell[i][j] == 1:
                dfs(i, j, 0)


    print('#{} {}'.format(tc, wire_sum))
    # 1 12
    # 2 10
    # 3 24