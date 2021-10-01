import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = float(input())

    ans = ''
    for j in range(1, 13):
        if N >= (2**(-j)):
            N = N - (2**(-j))
            ans += '1'
        else:
            ans += '0'
        if N == 0:
            break

    print('#{}'.format(tc), end=' ')
    if N != 0:
        print('overflow')
    else:
        print(ans)