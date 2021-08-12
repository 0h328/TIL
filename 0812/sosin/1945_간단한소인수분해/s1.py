# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pl0Q6ANQDFAUq&categoryId=AV5Pl0Q6ANQDFAUq&categoryType=CODE&problemTitle=1945&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
import sys
sys.stdin = open('input.txt')
INF = int(1e9)
for T in range(int(input())):
    result = [0]*5
    target = int(input())
    prime = [2, 3, 5, 7, 11]
    for i in range(5):
        for k in range(1, INF):
            if target%(prime[i]**k):
                result[i] = k-1
                break

    print('#{}'.format(T+1), end=' ')
    print(*result)

#1 3 2 2 3 1
#2 6 1 2 3 0
#3 6 4 2 0 1
#4 0 0 2 3 0
#5 0 3 4 0 1
#6 4 4 1 0 0
#7 7 3 0 3 0
#8 0 8 0 0 0
#9 0 0 2 0 0
#10 1 3 3 2 0
