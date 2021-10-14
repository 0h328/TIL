import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost_map = [list(map(int, input().split())) for _ in range(N)]
    # print(cost_map)
    visited = [[0] * N for i in range(N)]

    print('#{} {}'.format(tc, ))


#1 5
#2 8
#3 9

'''
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(x, y, cost):
    global min_cost

    visited[x][y] = 1

    if x == N-1 and y == N-1:
        if min_cost > cost:
            min_cost = cost
            return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            if cost_map[nx][ny] > cost_map[x][y]:
                visited[nx][ny] = 1
                DFS(nx, ny, cost + 1 + cost_map[nx][ny] - cost_map[x][y])
                visited[nx][ny] = 0
            else:
                visited[nx][ny] = 1
                DFS(nx, ny, cost + 1)
                visited[nx][ny] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost_map = [list(map(int, input().split())) for _ in range(N)]
    # print(cost_map)
    visited = [[0] * N for i in range(N)]

    min_cost = 987654321

    DFS(0, 0, 0)

    print('#{} {}'.format(tc, min_cost))
'''


