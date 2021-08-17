import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    tc = int(input())
    row_arr = [input() for _ in range(100)]
    col_arr = list(zip(*row_arr))
    max_palindrome = 1


    for i in range(100):
        for j in range(100-max_palindrome+1):
            if row_arr[i][j:j+max_palindrome] == row_arr[i][j:j+max_palindrome][::-1]:
                max_palindrome += 1
        ret1 = max_palindrome


    for i in range(100):
        for j in range(100-max_palindrome+1):
            if col_arr[i][j:j+max_palindrome] == col_arr[i][j:j+max_palindrome][::-1]:
                max_palindrome += 1
        ret2 = max_palindrome

    print('#{} {}'.format(tc, max(ret1, ret2)))





