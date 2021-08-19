def rectangle_paper(n):
    if n == 1:
        return 1
    if n == 2:
        return 3

    return rectangle_paper(n-1) + 2 * rectangle_paper(n-2)


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n = N // 10

    print('#{} {}'.format(tc, rectangle_paper(n)))