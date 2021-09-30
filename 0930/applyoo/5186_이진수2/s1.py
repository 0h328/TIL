import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    ans = ''
    i = -1
    while i > -15 and N:
        x = 2**i
        if N >= x:
            N -= x
            ans += '1'
        else:
            ans += '0'
        i -= 1

    print('#{0} {1}'.format(tc, ans if len(ans) < 13 else 'overflow'))
