import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = float(input())
    cnt = 1
    ans = ''
    while N != 0:
        if N - 2 ** (-cnt) > 0:
            N -= 2 ** (-cnt)
            cnt += 1
            ans += '1'

        elif N - 2 ** (-cnt) == 0:
            N -= 2 ** (-cnt)
            ans += '1'

        else:
            cnt += 1
            ans += '0'

    if cnt > 12:
        ans = 'overflow'

    print('#{} {}'.format(test_case, ans))