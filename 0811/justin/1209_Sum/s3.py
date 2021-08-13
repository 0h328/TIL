def max_sum(numbers):
    max_num = 0  # 최댓값 초기화
    N = 100  # 리스트 크기
    row_sum = col_sum = dg1_total = dg2_total = 0  # 가로 / 세로 / 대각선 2개 총합 초기화

    for i in range(N):  # 배열 크기만큼 반복을 돌며
        dg1_total += numbers[i][i]  # 대각선의 합 구하기
        dg2_total += numbers[N-1-i][N-1-i]
        for j in range(N):          # 다시 반복하며
            row_sum += numbers[i][j]  # 가로 합
            col_sum += numbers[j][i]  # 세로 합

        if row_sum > max_num:  # (합을 구한 이후) 가로 최댓값 구하고
            max_num = row_sum
        if col_sum > max_num:  # 세로 최댓값을 구하자
            max_num = col_sum

        row_sum = col_sum = 0  # 가로 & 세로 값은 다시 초기화 (하지 않으면 기존 값에 계속 누적)

    if dg1_total > max_num:  # 최종적으로 대각선과의 최댓값 구하기
        max_num = dg1_total
    if dg2_total > max_num:
        max_num = dg2_total
    return max_num

import sys
sys.stdin = open('input.txt')
for _ in range(1, 11):
    tc = int(input())
    numbers = [list(map(int, input().split())) for _ in range(100)]
    ans = max_sum(numbers)
    print('#{} {}'.format(tc, ans))