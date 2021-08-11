import sys

sys.stdin = open('input.txt')

for t in range(10):
    test_case = int(input())
    test_num = []

    for _ in range(100):
        test_num.append(list(map(int, input().split())))

    my_sum_row = my_sum_col = 0
    my_diag_pos = my_diag_neg = 0

    for i in range(100):
        temp_sum_row = temp_sum_col = 0
        for j in range(100):
            temp_sum_row += test_num[i][j]
            temp_sum_col += test_num[j][i]
            if i == j:
                my_diag_pos += test_num[i][j]
            if i == 100-j-1:
                my_diag_neg += test_num[i][j]

        if my_sum_row < temp_sum_row:
            my_sum_row = temp_sum_row
        if my_sum_col < temp_sum_col:
            my_sum_col = temp_sum_col

    my_max = max(my_sum_row, my_sum_col, my_diag_pos, my_diag_neg)


    print('#{0} {1}'.format(t + 1, my_max))
