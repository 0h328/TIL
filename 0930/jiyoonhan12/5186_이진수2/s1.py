import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = float(input())
    ans = 'overflow'

    temp = 0
    bin = ''
    for i in range(1, 13):
        step = (1/2)**i
        if N > temp + step: # 현재 step 표시할 수 있을 때
            temp += step
            bin += '1'
        elif N < temp + step:
            bin += '0'
        else: # 같을 때
            bin += '1'
            ans = bin
            break

    print('#{} {}'.format(t, ans))