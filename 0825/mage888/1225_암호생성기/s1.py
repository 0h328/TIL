import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    pw = list(map(int, input().split()))
    M = len(pw)

    k = 0
    while pw[-1] > 0:
        k = (k+1) % 6

        if k:
            pw.append(pw.pop(0)-k)

    if pw[-1] < 0:
        pw[-1] = 0
    print('#{}'.format(tc), end=' ')
    print(*pw)









