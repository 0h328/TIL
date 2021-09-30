import sys
sys.stdin = open('input.txt')


def decimal_to_binary(num):
    while num:
        num = (num * 2)
        int_num = int(num)

        if num >= 1:
            num -= 1

        answer.append(str(int_num))
        
        


T = int(input())

for tc in range(1, T+1):
    num = float(input())
    answer = []

    decimal_to_binary(num)


    if len(answer) >= 13:
        answer = 'overflow'
    else:
        answer = ''.join(answer)
    
    print('#{} {}'.format(tc, answer))