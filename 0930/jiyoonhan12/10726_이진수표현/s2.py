import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    i = 0
    while i != N:
        if M & (1 << i) and i == N-1:
            print('#{} ON'.format(t))
        elif not M & (1 << i):
            print('#{} OFF'.format(t))
            break
        i += 1