import sys

sys.stdin = open('input.txt')

T = int(input())

def check_row(data, N, M):
    palindrome = []
    for row in range(N):
        if M % 2:       # M 홀수일 때
            for col in range(M//2, N - M//2):
                chk_row = ''
                for i in range(1, M//2 + 1):
                    if data[row][col - i] != data[row][col + i]:
                        chk_row = ''
                        break
                    chk_row += data[row][col - i]
                if chk_row:
                    palindrome.append(chk_row[::-1] + data[row][col] + chk_row)
        else:       # M 짝수일 때
            for col in range(M//2 - 1, N - M//2):
                chk_row = ''
                for i in range(0, M//2):
                    if data[row][col - i] != data[row][col + i + 1]:
                        chk_row = ''
                        break
                    chk_row += data[row][col - i]
                if chk_row:
                    palindrome.append(chk_row[::-1] + chk_row)

    if palindrome:
        return palindrome

def check_col(data, N, M):
    palindrome = []
    for col in range(N):
        if M % 2:
            for row in range(M//2, N - M//2):
                chk_col = ''
                for i in range(1, M//2 + 1):
                    if data[row - i][col] != data[row + i][col]:
                        chk_col = ''
                        break
                    chk_col += data[row - i][col]
                if chk_col:
                    palindrome.append(chk_col[::-1] + data[row][col] + chk_col)
        else:
            for row in range(M//2 - 1, N - M//2 + 1):
                chk_col = ''
                for i in range(0, M//2):
                    if data[row - i][col] != data[row + i + 1][col]:
                        chk_col = ''
                        break
                    chk_col += data[row - i][col]
                if chk_col:
                    palindrome.append(chk_col[::-1] + chk_col)

    if palindrome:
        return palindrome

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    palindrome = []
    if check_row(data, N, M):
        palindrome += check_row(data, N, M)
    if check_col(data, N, M):
        palindrome += check_col(data, N, M)

    print('#{} {}'.format(tc, *palindrome))