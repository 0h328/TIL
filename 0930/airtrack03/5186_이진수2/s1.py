import sys
sys.stdin = open('input.txt')

T = int(input())

def float_to_binary(target):
    cnt = 0
    result = ''
    while cnt < 13:
        cnt += 1
        if target >= 2 ** (-cnt):
            target -= 2 ** (-cnt)
            result += '1'
        else:
            result += '0'
        if target == 0.0:
            return result
    return 'overflow'


for tc in range(1, T+1):
    data = float(input())

    ans = float_to_binary(data)

    print('#{} {}'.format(tc, ans))