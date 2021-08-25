import sys

sys.stdin = open('input.txt')


def check(y, x):
    return 0 <= y < N and 0 <= x < N


def DFS(y, x):
    stack = [(y, x)]
    visit = []

    while stack:
        y, x = stack.pop()
        if (y, x) not in visit:
            visit.append((y, x))

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if check(ny, nx):
                    if data[ny][nx] == 3:
                        return 1
                    elif data[ny][nx] == 0:
                        stack.append((ny, nx))
    return 0


for test in range(1, 1 + int(input())):
    N = int(input())

    data = [list(map(int, input())) for _ in range(N)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                y, x = i, j
    print('#{} {}'.format(test, DFS(y, x)))
