def solve(data):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    total_sum = 0      # 최종합

    for r in range(N):
        for c in range(N):
            abs_sum = 0
            for i in range(4):       # r, c를 중심으로 4방 탐색
                center = data[r][c]  # 중심값 구하고
                nr = r + dr[i]       # col & row 이동
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:     # 벽 처리
                    around = data[nr][nc]           # 주변값 가져오기
                    abs_sum += abs(center - around) # 그 값을 abs_sum에 누적
            total_sum += abs_sum
    return total_sum

import sys
sys.stdin = open('input2.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 가장 자리를 포함하여 계산 - 240
    ans = solve(data)
    print('#{} {}'.format(tc, ans))