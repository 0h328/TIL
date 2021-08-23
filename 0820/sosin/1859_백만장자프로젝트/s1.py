# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=1859&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    N = int(input())
    price_list = list(map(int, input().split()))
    max_price = 0
    answer = 0
    for p in reversed(price_list):
        if p > max_price:
            max_price = p
        else:
            answer += max_price - p

    print('#{} {}'.format((T+1), answer))

#1 4053
#2 6385
#3 26725
#4 211514
#5 4848198
#6 49761546
#7 500155606
#8 4995241394
#9 4999367498
#10 4995633799
