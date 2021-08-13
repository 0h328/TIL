import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a = b = c = d = e =0
    while N > 1:
        if N % 2 == 0:
            a += 1
            N //= 2
        if N % 3 == 0:
            b += 1
            N //= 3
        if N % 5 == 0:
            c += 1
            N //= 5
        if N % 7 == 0:
            d += 1
            N //= 7
        if N % 11 == 0:
            e += 1
            N //= 11
    print('#{} {} {} {} {} {}'.format(test_case, a, b, c, d, e))
