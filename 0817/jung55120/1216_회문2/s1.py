import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    n = 100

    row_str_list = [list(input()) for _ in range(n)]
    col_str_list = list(zip(*row_str_list))
    # print(col_str_list)

    result = 1 # 최소의 회문 값은 1

    palindrome_list = []

    for i in range(0, n): # 0 ~ 100행까지 반복
        for j in range(i + 1):
            for k in range(n-j, n):
                # if row_str_list[i][l:k+i//2] == row_str_list[i][l:k+i//2][::-1]:
                #     print(True)


