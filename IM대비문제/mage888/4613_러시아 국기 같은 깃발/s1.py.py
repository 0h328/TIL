import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]

    min_value = N*M+1

    white_cnt = 0
    for w in range(N-2):
        for i in range(M):
            if data[w][i] != 'W':
                white_cnt += 1

        blue_cnt = 0
        for b in range(w+1, N-1):
            for j in range(M):
                if data[b][j] != 'B':
                    blue_cnt += 1

            red_cnt = 0
            for r in range(b+1, N):
                for k in range(M):
                    if data[r][k] != 'R':
                        red_cnt += 1

            total = white_cnt + blue_cnt + red_cnt

            if total < min_value:
                min_value = total

    print('#{} {}'.format(tc, min_value))
