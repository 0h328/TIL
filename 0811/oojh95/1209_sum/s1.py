import sys
sys.stdin = open('input.txt')

T = 10
for _ in range(T):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_result = 0
    sum_diag = 0
    sum_revdiag = 0
    for i in range(100):
        sum_row = 0
        sum_col = 0
        for j in range(100):
            sum_row += arr[i][j]
            sum_col += arr[j][i]
            if i == j:
                sum_diag += arr[i][j]
            if i + j == 99:
                sum_revdiag += arr[i][j]
        if max_result < sum_row:
            max_result = sum_row
        if max_result < sum_col:
            max_result = sum_col
    if max_result < sum_diag:
        max_result = sum_diag
    if max_result < sum_revdiag:
        max_result = sum_revdiag
    print('#{} {}'.format(test_case, max_result))