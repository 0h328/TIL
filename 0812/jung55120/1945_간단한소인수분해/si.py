import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC+1):
    num = int(input())

    cnt_list = [0] * 5

    while num > 1:
        if num % 2 == 0:
            cnt_list[0] += 1
            num = num / 2
        elif num % 3 == 0:
            cnt_list[1] += 1
            num = num / 3
        elif num % 5 == 0:
            cnt_list[2] += 1
            num = num / 5
        elif num % 7 == 0:
            cnt_list[3] += 1
            num = num / 7
        elif num % 11 == 0:
            cnt_list[4] += 1
            num = num / 11

    num_str = ''
    for i in range(len(cnt_list)):
        num_str += str(cnt_list[i]) + str(' ')

    print('#{0} {1}'.format(tc, num_str))