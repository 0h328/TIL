import sys
sys.stdin=open('input.txt')

for test in range(1,1+int(input())):
    N,M = map(int,input().split())
    weight = list(map(int,input().split()))
    maximum = list(map(int,input().split()))

    answer = 0
    for i in range(M):
        temp = 0
        for j in weight:
            if maximum[i] >= j and j >= temp:
                temp = j
        if temp !=0:
            weight.remove(temp)
        answer += temp

    print('#{} {}'.format(test,answer))