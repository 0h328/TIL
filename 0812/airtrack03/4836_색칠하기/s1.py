import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    area = [[0] * 10 for _ in range(10)]
    N = int(input())
    purple = []

    for _ in range(N):
        x_start, y_start, x_end, y_end, color = map(int, input().split())
        for y in range(y_start, y_end + 1):
            for x in range(x_start, x_end + 1):
                area[y][x] += color
                if area[y][x] >= 3 and (x, y) not in purple:    # 이미 보라색인데 또 덧칠했을 때 중복해서 더해지는 것 방지
                    purple.append((x, y))
    ans = len(purple)

    print('#{} {}'.format(tc, ans))