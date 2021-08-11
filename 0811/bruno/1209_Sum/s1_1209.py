import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_d1 = sum_d2 = 0             # 양 대각선의 합 초기화
    max_sum_r = max_sum_c = 0       # 행합, 열합의 최댓값 초기화

    for i in range(100):            # i는 행번호
        sum_r = sum_c = 0           # 행, 열의 합 초기화
        sum_d1 += arr[i][i]         # 1번 대각선의 합 / j == i
        sum_d2 += arr[i][99 - i]    # 2번 대각선의 합 / j == 99-i

        for j in range(100):        # j는 열번호
            sum_r += arr[i][j]      # 행합
            sum_c += arr[j][i]      # 열합

        if sum_r > max_sum_r:       # 행합 최댓값
            max_sum_r = sum_r
        if sum_c > max_sum_c:       # 열합 최댓값
            max_sum_c = sum_c

    print('#{} {}'.format(tc, max(max_sum_r, max_sum_c, sum_d1, sum_d2)))
    break