import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 'OFF'
    for i in range(N):
        if M % 2 == 0:
            break
        M //= 2
    else:
        ans = 'ON'

    print('#{} {}'.format(tc, ans))