# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE&problemTitle=1979&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_T = list(zip(*arr))
    result = []
    for row in [*arr, *arr_T]:
        k = 0
        for i in row:
            if i:
                k+=1
            else:
                result.append(k)
                k=0
        else:
            if k:
                result.append(k)

    print('#{} {}'.format((T+1), result.count(K)))

#1 2
#2 6
#3 6
#4 0
#5 14
#6 2
#7 45
#8 0
#9 98
#10 7