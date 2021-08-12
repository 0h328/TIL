# 중앙값 기준으로 상하좌우 값을 빼준 값의 절대값의 합
import sys

sys.stdin = open('input2.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    for i in range(N):
        for j in range(N):
            x = j
            y = i
            for d in range(4):
                nxt_x = x + dx[d]
                nxt_y = y + dy[d]
                if 0 <= nxt_x < N and 0 <= nxt_y < N:
                    ans += abs(data[nxt_y][nxt_x] - data[y][x])
                else:
                    continue

    print('#{} {}'.format(tc, ans))