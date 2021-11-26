'''
sum(), zip() 사용하지 않음

1. 입력값을 배열로 받는다.
2. 최댓값을 저장하는 변수 하나 생성
3. 행을 탐색하여 각 행의 합을 최댓값과 비교
4. 열을 탐색하여 각 열의 합을 최댓값과 비교
5. 대각선의 합을 최댓값과 비교
'''

import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    test_case = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0

    left_diagonal = 0  # 왼쪽 대각선 합계
    right_diagonal = 0  # 오른쪽 대각선 합계

    for i in range(100):
        row_sum1 = 0                # 행 합계
        col_sum2 = 0                # 열 합계

        for j in range(100):
            row_sum1 += li[i][j]
            col_sum2 += li[j][i]

        left_diagonal += li[i][i]
        right_diagonal += li[i][-1-i]

        if max_sum < row_sum1:
            max_sum = row_sum1
        if max_sum < col_sum2:
            max_sum = col_sum2
        if max_sum < left_diagonal:
            max_sum = left_diagonal
        if max_sum < right_diagonal:
            max_sum = right_diagonal

    print('#{} {}'.format(test_case, max_sum))