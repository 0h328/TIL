import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0]*8
    for i in range(8):
        if n // money[i] == 0:
            continue
        else:
            result[i] = n // money[i] # result에 몫을 담는다
            n %= money[i]
    print('#{}'.format(tc+1))
    print(*result)