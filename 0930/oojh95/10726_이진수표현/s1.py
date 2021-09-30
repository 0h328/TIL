import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    while N > 0:
        if (M % 2) & 1:
            N -= 1
            M //= 2
        else:
            break
    if N > 0:
        result = 'OFF'
    else:
        result = 'ON'
    print('#{} {}'.format(tc, result))
