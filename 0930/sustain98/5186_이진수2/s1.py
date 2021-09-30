import sys, math
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    number = float(input())
    res = ''
    div = -1
    while (not math.isclose(number, 0)) and len(str(res)) < 13:
        quo, number = divmod(number, 2**div)
        res += str(int(quo))
        div -= 1

    if len(str(res)) < 13:
        print('#{} {}'.format(idx, res))
    else:
        print('#{} {}'.format(idx, 'overflow'))