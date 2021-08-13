import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T + 1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    dx = [1, -1, 0]
    dy = [0, 0, -1]

    for i in range(100):
        if arr[99][i] == 2:
            x = i
            break
    y = 99

    while y > 0:
        if x == 0:
            if arr[y][x + 1] == 1:
                while True:
                    x += dx[0]
                    y += dy[0]
                    if arr[y - 1][x] == 1:
                        break
                y -= 1
            else:
                x += dx[2]
                y += dy[2]
        elif x == 99:
            if arr[y][x - 1] == 1:
                while True:
                    x += dx[1]
                    y += dy[1]
                    if arr[y-1][x] == 1:
                        break
                y -= 1
            else:
                x += dx[2]
                y += dy[2]
        elif arr[y][x-1] == 1:
            while True:
                x += dx[1]
                y += dy[1]
                if arr[y - 1][x] == 1:
                    break
            y -= 1
        elif arr[y][x+1] == 1:
            while True:
                x += dx[0]
                y += dy[0]
                if arr[y - 1][x] == 1:
                    break
            y -= 1
        else:
            x += dx[2]
            y += dy[2]

    print('#{} {}'.format(test_case, x))



