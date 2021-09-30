import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    N, M = map(int, input().split())

    for i in range(N):
        if not(M & (1<<i)):
            print('#{} {}'.format(case + 1, 'OFF'))
            break
    else:
        print('#{} {}'.format(case + 1, 'ON'))
