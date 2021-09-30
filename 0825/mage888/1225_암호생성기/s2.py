import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    pw = list(map(int, input().split()))

    k = 0
    while pw[-1] > 0:
        k %= 5
        k += 1
        pw.append(pw.pop(0)-k)

    pw[-1] = 0
    print('#{} {}'.format(tc, ' '.join(map(str, pw))))