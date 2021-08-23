# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE&problemTitle=1974&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(9)]
    arr_T = list(zip(*arr))
    arr_box = []
    for i in range(3):
        for j in range(3):
            temp = []
            for k in range(3):
                for l in range(3):
                    temp.append(arr[3*i+k][3*j+l])
        arr_box.append(temp)

    result = 1
    for row in [*arr, *arr_T, *arr_box]:
        if len(set(row)) - 9:
            result = 0
            break

    print('#{} {}'.format((T+1), result))

#1 1
#2 0
#3 1
#4 0
#5 0
#6 1
#7 0
#8 1
#9 1
#10 0
