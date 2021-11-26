import sys

sys.stdin = open('input.txt')

T = int(input())

for test in range(T):
    N = int(input())

    empty = [[0]*10 for i in range(10)]

    for i in range(N):
        data = list(map(int,input().split()))

        for r in range(abs(data[0]-data[2])+1):
            for c in range(abs(data[1]-data[3])+1):
                empty[data[0]+r][data[1]+c] += data[4]

    cnt = 0
    for i in range(len(empty)):
        for j in range(len(empty[i])):
            if empty[i][j] == 3:
                cnt+=1

    print('#{} {}'.format(test+1,cnt))
