import sys
sys.stdin = open('input.txt')

for t in range(10):
    case = int(input())

    arr = [] # 2차원 배열 안에 숫자 채우기
    for num in range(100):
        in_arr = list(map(int, input().split()))
        arr.append(in_arr)

    compare_sum = []

    for i in range(100): # 각 행의 합
        row_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
        compare_sum.append(row_sum)

    for j in range(100): # 각 열의 합
        col_sum = 0
        for i in range(100):
            col_sum += arr[i][j]
        compare_sum.append(col_sum)

    diag_sum1 = 0 # 오른쪽 아래로 내려가는 대각선
    for i in range(100):
        for j in range(100):
            if i == j:
                diag_sum1 += arr[i][j]
    compare_sum.append(diag_sum1)

    diag_sum2 = 0 # 오른쪽 위로 올라가는 대각선
    for i in range(100):
        for j in range(100):
            if i + j == 99:
                diag_sum2 += arr[i][j]
    compare_sum.append(diag_sum2)

    print('#{} {}'.format(case, max(compare_sum)))