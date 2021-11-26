import sys
sys.stdin = open('input.txt')

def find_palindrome():

    for i in range(len(row_list)):
        for j in range(N-M+1):
            if row_list[i][j:j+M] == row_list[i][j:j+M][::-1]:
                return row_list[i][j:j+M]

    for i in range(len(col_list)):
        for j in range(N-M+1):
            if col_list[i][j:j+M] == col_list[i][j:j+M][::-1]:
                return col_list[i][j:j+M]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    row_list = [input() for _ in range(N)]

    col_list = []
    for i in range(len(row_list)):
        col_str = ''
        for j in range(len(row_list[i])):
            col_str += row_list[j][i]
        col_list.append(col_str)

    print('#{} {}'.format(tc, find_palindrome()))