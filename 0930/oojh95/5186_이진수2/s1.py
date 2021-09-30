import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = float(input())
    tmp = 1/2
    cnt = ''
    while N > 0:
        if N >= tmp:
            N -= tmp
            cnt += '1'
            tmp /= 2
        else:
            tmp /= 2
            cnt += '0'
    if len(cnt) > 12:
        cnt = 'overflow'
    print('#{} {}'.format(tc, cnt))