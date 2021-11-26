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
                # 같은 색이 중복해서 칠해지지 않도록 조건 필요
                if area[y][x] == color or area[y][x] == 3:  # 칠하려던 색으로 같은 색이 칠해져 있거나 이미 보라색인 경우
                    continue
                area[y][x] += color     # 다른 색이 칠해져있거나 아무 것도 칠해져있지 않은 경우
                if area[y][x] == 3:    # 위 조건 추가로 더이상 보라색 위에 덧칠해지는 경우 없으므로 not in 불필요
                    purple.append((x, y))
    ans = len(purple)

    print('#{} {}'.format(tc, ans))