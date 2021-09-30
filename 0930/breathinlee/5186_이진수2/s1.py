import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    ans = ''
    for d in range(1, 13):
        # ans += str(int(N // (2**(-d))))
        ans += str(int(N * (2**d)))
        N %= (2**(-d))
        if N:
            continue
        else:
            break
    else:
        ans = 'overflow'

    print('#{} {}'.format(tc, ans))








