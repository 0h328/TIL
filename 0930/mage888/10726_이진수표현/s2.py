import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    cnt = 0
    for i in range(N):
        if M & (1 << i):
            cnt += 1

    if cnt == N:
        print('#{} ON'.format(tc))
    else:
        print('#{} OFF'.format(tc))


