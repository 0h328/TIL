# for문 1번 사용하기!
import sys

sys.stdin = open('input.txt')

T = 10

for _ in range(T):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    data_rotate = list(zip(*data))    # col sum 계산을 위해 rotate

    diagonal = 0
    diagonal_reverse = 0
    ans = 0

    for i in range(100):
        sum_row = sum(data[i])
        sum_col = sum(data_rotate[i])
        if ans < sum_row:
            ans = sum_row
        if ans < sum_col:
            ans = sum_col
        diagonal += data[i][i]
        diagonal_reverse += data[i][99-i]

    if diagonal > ans:
        ans = diagonal
    if diagonal_reverse > ans:
        ans = diagonal_reverse

    print('#{} {}'.format(tc, ans))