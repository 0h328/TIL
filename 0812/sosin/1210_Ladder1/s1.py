# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh&categoryId=AV14ABYKADACFAYh&categoryType=CODE&problemTitle=1210&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())

    ladders = [list(map(int, input().split())) for _ in range(100)]
    
    r = 99
    for c in range(100):
        if ladders[-1][c] == 2:
            break

    is_left = False
    is_right = False
    while r > 0:
        if is_left:
            if c-1 >= 0 and ladders[r][c-1]:
                r, c = r, c-1
            else:
                is_left=False
                r, c = r-1, c
        elif is_right:
            if c+1 < 100 and ladders[r][c+1]:
                r, c = r, c+1
            else:
                is_right=False
                r, c = r-1, c
        else:
            if c-1 >= 0 and ladders[r][c-1]:
                r, c = r, c-1
                is_left = True
            elif c+1 < 100 and ladders[r][c+1]:
                r, c = r, c+1
                is_right = True
            else:
                r, c = r-1, c

    print('#{} {}'.format(T, c))

#1 67
#2 45
#3 39
#4 24
#5 91
#6 93
#7 90
#8 4
#9 99
#10 35
