import sys
sys.stdin = open('input.txt')

def find_miro(x, y):
    global result, visited
    Q.append((x, y))
    visited((x, y))

    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:  # length 범위 안에 있고, 미로의 수가 1이 아닐 때
                if miro[nx][ny] != 1 and [nx, ny] not in visited:
                    Q.append([nx, ny])
                    visited.append([nx, ny])
                    distance[nx][ny] = distance[x][y] + 1
                    if miro[nx][ny] == 3:
                        result = distance[x][y]
                        return

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    distance = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    Q = []
    result = 0

    # print(miro)

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2: # 2의 위치 찾기
                x, y = i, j

    print('#{} {}'.format(tc, find_miro(x, y)))
                # print(i, j)
    # ????? 왜 안되지????

    # find_miro(1, 1)

