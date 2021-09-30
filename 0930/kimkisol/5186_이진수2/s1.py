import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = float(input())
    result = ''
    bin_num = 0.5
    cnt = 0

    while N > 0:
        if N >= bin_num:
            N -= bin_num
            result += '1'
        else:
            result += '0'
        bin_num /= 2
        cnt += 1
        if cnt > 13:
            result = 'overflow'
            break

    print('#{} {}'.format(t, result))