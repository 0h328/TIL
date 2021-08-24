import sys
sys.stdin = open("input.txt")

T = int(input())

for num in range(T):
    N, K = map(int, input().split())
    array = []
    for _ in range(N):
        arr = list(map(int, input().split()))
        array.append(arr)
    col_array = list(zip(*array))
    col_list = []
    for arr in array:
        arr.append(0)
    for col_arr in col_array:
        col_lst = list(col_arr)
        col_list.append(col_lst)
    for col_lst in col_list:
        col_lst.append(0)

    cnt = 0

    for i in range(N):
        for j in range(N):
            if array[i][j] == 1:
                if array[i][j-1] == 0 and array[i][j+1] == 1 and array[i][j+2] == 1 and array[i][j+3] == 0:
                    cnt+=1

            if col_list[i][j] == 1:
                if col_list[i][j-1] == 0 and col_list[i][j+1] == 1 and col_list[i][j+2] == 1 and col_list[i][j+3] == 0:
                    cnt+=1
    print('#{} {}'.format(num+1, cnt))



