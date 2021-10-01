import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    if bin(M)[-N:].count('1') == N:
        print('#{} ON'.format(tc))
    else:
        print('#{} OFF'.format(tc))
