# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_65wkqsb4DFAWS&categoryId=AV_65wkqsb4DFAWS&categoryType=CODE&problemTitle=3143&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

import sys
sys.stdin = open('input.txt')


def miniTyping(str1, str2):
    return str1.count(str2) + len(str1.replace(str2, '')) # 포함된 개수 + str1(str2 공백 처리한 길이 반환)


T = int(input())
for test in range(T):
    str1, str2 = map(str, input().split())
    print('#{} {}'.format(test+1, miniTyping(str1, str2)))