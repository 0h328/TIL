import sys
sys.stdin = open('input.txt')


T = int(input())
answer = []

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pair = list(map(int, input().split()))

    li = [i for i in range(N+1)]        # 학생들 번호
    
    for idx in range(len(pair)//2):
        x = pair[idx*2]                 # student 1
        y = pair[idx*2+1]               # student 2

        if x > y:                       # if student 1 greater than student 2
            x, y = y, x                 # swap

        while li[x] != x:               # if alone student 
            x = li[x]                   # 
        li[y] = x

        for k in range(len(li)):        #
            if li[k] == y:
                li[k] = x

    print(li)
    print(set(li))
    answer.append('#{} {}'.format(tc, len(set(li))-1))

print(*answer, sep='\n')