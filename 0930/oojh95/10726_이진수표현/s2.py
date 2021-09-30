import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    for i in range(N):
        if M & (1<<i):
            continue
        else:
            result = 'OFF'
            break
    else:
        result = 'ON'
    print('#{} {}'.format(tc, result))