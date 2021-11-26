import sys

sys.stdin = open('input.txt')

T = int(input())


def cal_num2(a):
    temp = 0
    for i in range(len(a)):
        temp += int(num_2[i]) * 2 ** (i)
    return (temp)


def cal_num3(a):
    temp = 0
    for i in range(len(a)):
        temp += int(num_3[i]) * 3 ** (i)
    return (temp)


for tc in range(1, T + 1):
    ans = 0
    num_2 = []
    num_3 = []
    num_2.extend((input()))
    num_3.extend((input()))
    num_2 = num_2[::-1]
    num_3 = num_3[::-1]
    list_3 = ['0', '1', '2']
    for i in range(len(num_2)):
        if num_2[i] == '1':
            num_2[i] = '0'
        else:
            num_2[i] = '1'
        temp_num1 = cal_num2(num_2)
        if num_2[i] == '1':
            num_2[i] = '0'
        else:
            num_2[i] = '1'

        for b in range(len(num_3)):
            if num_3[b] == '0':
                num_3[b] = '1'
                temp_num2 = cal_num3(num_3)
                if temp_num1 == temp_num2:
                    ans = temp_num1
                    break
                num_3[b] = '2'
                temp_num2 = cal_num3(num_3)
                if temp_num1 == temp_num2:
                    ans = temp_num1
                    break
                num_3[b] = '0'
            elif num_3[b] == '1':
                num_3[b] = '2'
                temp_num2 = cal_num3(num_3)
                if temp_num1 == temp_num2:
                    ans = temp_num1
                    break
                num_3[b] = '0'
                temp_num2 = cal_num3(num_3)
                if temp_num1 == temp_num2:
                    ans = temp_num1
                    break
                num_3[b] = '1'
            else:
                num_3[b] = '0'
                temp_num2 = cal_num3(num_3)
                if temp_num1 == temp_num2:
                    ans = temp_num1
                    break
                num_3[b] = '1'
                temp_num2 = cal_num3(num_3)
                if temp_num1 == temp_num2:
                    ans = temp_num1
                    break
                num_3[b] = '2'
        if ans != 0:
            break
    print('#{} {}'.format(tc,ans))