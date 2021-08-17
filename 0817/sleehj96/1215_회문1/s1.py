import sys


def check_palindrome(lst, n):
    cnt = 0
    for i in range(len(lst)-n+1):
        for j in range(n//2):
            if lst[i+j] != lst[i+n-1-j]:
                break
        else:
            cnt += 1

    return cnt


sys.stdin = open('input.txt')

T = 10
case_num = 1
while case_num <= T:
    palindrome_len = int(input())
    char_grid = [list(input()) for _ in range(8)]
    char_grid_tp = zip(*char_grid)

    my_sum = 0
    for row in char_grid:
        my_sum += check_palindrome(row, palindrome_len)

    for col in char_grid_tp:
        my_sum += check_palindrome(col, palindrome_len)

    print('#{0} {1}'.format(case_num, my_sum))
    case_num += 1
