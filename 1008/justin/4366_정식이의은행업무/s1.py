def to_decimal(x, mode):
    value = 0
    for i in range(len(x)):
        value = value * mode + int(x[i])
    return value

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    str2 = input()                          # 2진수 & 3진수
    str3 = input()
    list2, list3 = [], []                   # 2진수, 3진수
    for i in range(len(str2)):              #2진수
        x2 = list(str2)
        x2[i] = str((int(x2[i]) + 1) % 2)
        list2.append(to_decimal(x2, 2))
        #list2.append(int(''.join(x2), 2))
    for i in range(len(str3)):              #3진수
        for j in [1, 2]:
            x3 = list(str3)
            x3[i] = str((int(x3[i]) + j) % 3)
            list3.append(to_decimal(x3, 3))
    for i in range(len(list2)):
        for j in range(len(list3)):
            if list2[i] == list3[j]:        # 같은값 찾기
                ans = list2[i]
                break
    print('#{} {}'.format(tc, ans))