import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    no, n = input().split()
    char_n = list(input().split())

    arr_list = []
    for i in char_n:
        if i == 'ZRO':
            arr_list.append(0)
        elif i == 'ONE':
            arr_list.append(1)
        elif i == 'TWO':
            arr_list.append(2)
        elif i == 'THR':
            arr_list.append(3)
        elif i == 'FOR':
            arr_list.append(4)
        elif i == 'FIV':
            arr_list.append(5)
        elif i == 'SIX':
            arr_list.append(6)
        elif i == 'SVN':
            arr_list.append(7)
        elif i == 'EGT':
            arr_list.append(8)
        elif i == 'NIN':
            arr_list.append(9)

    arr_list.sort()

    for i in range(len(arr_list)):
        if arr_list[i] == 0:
            arr_list[i] = 'ZRO'
        elif arr_list[i] == 1:
            arr_list[i] = 'ONE'
        elif arr_list[i] == 2:
            arr_list[i] = 'TWO'
        elif arr_list[i] == 3:
            arr_list[i] = 'THR'
        elif arr_list[i] == 4:
            arr_list[i] = 'FOR'
        elif arr_list[i] == 5:
            arr_list[i] = 'FIV'
        elif arr_list[i] == 6:
            arr_list[i] = 'SIX'
        elif arr_list[i] == 7:
            arr_list[i] = 'SVN'
        elif arr_list[i] == 8:
            arr_list[i] = 'EGT'
        elif arr_list[i] == 9:
            arr_list[i] = 'NIN'

    print('#{}'.format(tc))
    print(*arr_list)

