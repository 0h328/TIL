import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    ans = float(input())
    temp = 1
    ans_int = ''
    for i in range(1,13):
        temp = temp * 0.5
        if ans == 0:
            break
        elif temp <= ans:
            ans = ans-temp
            ans_int += str(1)
        else:
            ans_int += str(0)

    if ans != 0:
        print('#{} overflow'.format(tc))
    else:
        print('#{} {}'.format(tc,ans_int))

