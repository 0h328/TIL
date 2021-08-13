# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE&problemTitle=2001&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    N, M = map(int, input().split())
    paris = [list(map(int, input().split())) for _ in range(N)]
    max_paris = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            max_paris = max(max_paris, sum([sum(row[j:j+M]) for row in paris[i:i+M]]))
    print('#{} {}'.format((T+1), max_paris))

#1 49
#2 159
#3 428
#4 620
#5 479
#6 941
#7 171
#8 968
#9 209
#10 1242
