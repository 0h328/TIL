import sys

sys.stdin = open('input2.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]

    total = 0
    for i in range(n):
        for j in range(n):
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                else:
                    total += abs(data[i][j] - data[nx][ny])

    print('#{} {}'.format(tc, total))