import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    result = 'ON'

    while N > 0:
        if M % 2:
            N -= 1
            M //= 2
        else:
            result = 'OFF'
            break

    print('#{} {}'.format(t, result))