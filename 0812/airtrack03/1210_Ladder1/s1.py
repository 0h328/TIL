import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    N = 100
    ans = 0
    # 밑에서 2인 지점부터 시작하여 거꾸로 올라감
    x = ladder[99].index(2)
    y = 99
    visited = [[0]*N for _ in range(N)]

    while True:
        visited[y][x] += 1
        if x-1 >= 0 and ladder[y][x-1] == 1 and visited[y][x-1] == 0:
            x -= 1
            continue
        elif x+1 < N and ladder[y][x+1] == 1 and visited[y][x+1] == 0:
            x += 1
            continue
        else:
            y -= 1

        if y == 0:
            break
    ans = x

    print('#{} {}'.format(tc, ans))
