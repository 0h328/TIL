import sys

sys.stdin = open('input.txt')

T = 10

def check_palindrome(data, N, M, row):
    cnt = 0
    for i in range(N - M + 1):
        for j in range(M//2):
            if data[row][i+j] != data[row][i + M - 1 - j]:
                break
        else:       # 안쪽 for문이 다 돌면 길이 M짜리 회문이므로 cnt += 1
            cnt += 1

    return cnt

for tc in range(1, T+1):
    N = 8
    M = int(input())
    data = [list(input()) for _ in range(N)]
    data_reverse = list(zip(*data))

    ans = 0
    row = 0

    while row < N:
        ans += check_palindrome(data, N, M, row)
        ans += check_palindrome(data_reverse, N, M, row)
        row += 1

    print('#{} {}'.format(tc, ans))