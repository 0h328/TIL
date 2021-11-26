import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cnt = 0
    for j in range(N):
        if M & (1 << j):
            cnt += 1
    if cnt == N:
        print('#{} {}'.format(tc, 'ON'))
    else:
        print('#{} {}'.format(tc, 'OFF'))



#    if M%2:
#        print('#{} {}'.format(tc, 'ON'))
#    else:
#        print('#{} {}'.format(tc, 'OFF'))