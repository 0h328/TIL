import sys

sys.stdin = open('input.txt')

T = int(input())


def find_root(x, y):
    global check1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for k in range(4):
        new_x = x + dx[k]
        new_y = y + dy[k]
        if 0 <= new_x < N and 0 <= new_y < N and not maze[new_y][new_x] and check[new_y][new_x] != 1:
            check[new_y][new_x] = 1
            find_root(new_x, new_y)
        elif 0 <= new_x < N and 0 <= new_y < N and maze[new_y][new_x] == 3:
            check1 = 1
            return


for i in range(T):
    N = int(input())
    check1 = 0
    maze = [list(map(int, input())) for _ in range(N)]
    start_x = start_y = 0
    check = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if maze[y][x] == 2:
                start_x = x
                start_y = y
    find_root(start_x, start_y)
    print('#{} {}'.format(i+1,check1))
