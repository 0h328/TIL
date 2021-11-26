import sys
sys.stdin = open('input.txt')

def find_miro(x, y):
    global result
    if miro[x][y] == 3: # 만약 x, y좌표가 3이면 result = 1
        result = 1
        return          # 끝내기

    visited.append([x, y])

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < 16 and 0 <= ny < 16: # length 범위 안에 있고, 미로의 수가 1이 아닐 때
            if miro[nx][ny] != 1 and [nx, ny] not in visited:
                find_miro(nx, ny) # 재귀를 이용해 다시 반복


for tc in range(1, 11):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(16)]
    result = 0
    visited = []

    # print(miro)

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2: # 2의 위치 찾기
                find_miro(i, j)
                # print(i, j)
    # ????? 왜 안되지????

    # find_miro(1, 1)

    print('#{} {}'.format(tc, result))