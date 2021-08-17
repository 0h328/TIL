import sys
sys.stdin = open('input.txt')

def find_palindrome():

    for r in range(N):
        for i in range(N-M+1):
            for m in range(M//2):
                if row_list[r][i+m] != row_list[r][i+M-1-m]:
                    break
            else:
                result = ''
                for k in range(i, i+M):
                    result += row_list[r][k]
                return result

    for c in range(N):
        for j in range(N-M+1):
            for n in range(M//2):
                if col_list[c][j+n] != col_list[c][j+M-1-n]:
                    break
            else:
                result = ''
                for k in range(j, j+M):
                    result += col_list[c][k]
                return result

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    row_list = [input() for _ in range(N)]
    # print(row_list)

    col_list = []
    for i in range(len(row_list)):
        col_str = ''
        for j in range(len(row_list[i])):
            col_str += row_list[j][i]
        col_list.append(col_str)

    # print(col_list)
    print('#{} {}'.format(tc, find_palindrome()))


