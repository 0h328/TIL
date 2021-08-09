import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(T):
    N = int(input())

    numbers = list(map(int,input().split()))

    result = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(numbers[i]):
            if numbers[i] == 0:
                result[i][j] = 0
            else:
                result[i][j] = 1


    cntlist = []
    for j in range(N):
        cnt = 0
        for i in range(N):
            if result[i][j] == 1:
                for h in range(N-i):
                    if result[i+h][j] == 0:
                        cnt+=1
        cntlist.append(cnt)

    print(max(cntlist))

