import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = float(input())
    ans = ''

    i = -1
    while i >= -12:

        if N >= 2 ** i:
            N -= 2 ** i
            ans += '1'
        else:
            ans += '0'

        if N == 0:
            print('#{} {}'.format(tc + 1, ans))
            break
        i -= 1

    else:
        print('#{} {}'.format(tc + 1, 'overflow'))
    # break
