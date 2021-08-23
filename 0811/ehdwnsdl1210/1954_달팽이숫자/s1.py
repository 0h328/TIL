import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    S = [[0] * N for _ in range(N)]     # 2차원 배열

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]  # 우하좌상

    x, y = 0, 0     # 첫 좌표

    S[x][y] = 1     # 첫 값

    d = 0   # 0, 1, 2, 3 (우하좌상)

    i = 2   # 다음 값 (증가 진행)

    while i <= N * N:
        if -1 < x + dx[d % 4] < N and -1 < y + dy[d % 4] < N and S[x + dx[d % 4]][y + dy[d % 4]] == 0:
            x = x + dx[d % 4]
            y = y + dy[d % 4]       #?
            S[x][y] = i     # 값 입력
            i += 1      # 다음 값

        else:   # 벗어날 예정
            d += 1      # 우하좌상

    print('#{}'.format(tc + 1))
    for i in S:
        print(*i)