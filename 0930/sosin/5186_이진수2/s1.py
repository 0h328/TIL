import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    result = ''
    temp = float(input())
    for i in range(1, 13):
        if temp >= 2**-i:
            temp -= 2**-i
            result+='1'
        else:
            result+='0'

        if temp == 0:
            break

    else:
        result = 'overflow'

    print('#{} {}'.format((T+1), result))

#1 101
#2 overflow
#3 001