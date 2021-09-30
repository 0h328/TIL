import sys
sys.stdin = open("input.txt")


def bin(num1):
    global result
    while True:
        num2 = num1 * 2
        tmp = int(num2)
        result += str(tmp)
        num1 = num2 - tmp
        if num1 == 0.0:
            return

T = int(input())
for t in range(T):
    num = float(input())
    result = ''

    bin(num)

    if len(result) > 13:
        print('#{} overflow'.format(t+1))
    else:
        print('#{} {}'.format(t+1, result))