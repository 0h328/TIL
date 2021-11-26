import sys

sys.stdin = open('input.txt')

for test in range(1, 1 + int(input())):
    num = float(input())
    answer = ''

    for i in range(-1, -14, -1):
        if num == 0:
            break
        temp = str(int(num // (2 ** i)))
        answer += temp
        num %= (2 ** i)

    else:
        answer = 'overflow'

    print('#{} {}'.format(test, answer))
