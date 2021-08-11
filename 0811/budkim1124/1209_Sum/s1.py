import sys
sys.stdin = open('input.txt')


for num1 in range(1,11):
    arr = []
    N = int(input())

    for num2 in range(100):
        lst = list(map(int, input().split()))
        arr.append(lst)

    tot_arr = []

    for i in range(len(arr)):  # 행의 합
        tot_row = 0
        for j in range(len(arr)):
            tot_row += arr[i][j]
        tot_arr.append(tot_row)

    for i in range(len(arr)): #  열의 합
        tot_col = 0
        for j in range(len(arr)):
            tot_col += arr[j][i]
        tot_arr.append(tot_col)

    tot_x1 = 0
    for i in range(len(arr)): # 대각선 합
        for j in range(len(arr)):
            if i == j:
                tot_x1 += arr[i][j]
        tot_arr.append(tot_x1)

    tot_x2 = 0
    for i in range(len(arr)): # 대각선 합
        for j in range(len(arr)):
            if i+j == 99:
                tot_x2 += arr[i][j]
        tot_arr.append(tot_x2)

    print("#{} {}".format(num1, max(tot_arr)))