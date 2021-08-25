import sys
sys.stdin = open("input2.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    r, c = 0, 0

    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]  # 상하좌우

    sum_list = []

    for r in range(N):
        for c in range(N):
            for i in range(4):
                sum_value = 0
                nr = r + dr[i]
                nc = c + dc[i]
                if (0 <= nr < N) and (0 <= nc < N):
                    my_value = abs(data[r][c] - data[nr][nc])
                    sum_value += my_value
                    sum_list.append(sum_value)
                else:
                    continue
    print('#{} {}'.format(tc, sum(sum_list)))





