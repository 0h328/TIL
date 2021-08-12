import sys

sys.stdin = open('input.txt')

T = int(input())

for test in range(T):
    N = int(input())
    data = list(map(int,input().split()))

    for i in range(len(data)-1):
        if not i&1:
            maxi=i
            for j in range(i+1,len(data)):
                if data[j] > data[maxi]:
                    maxi=j
            data[i],data[maxi] = data[maxi],data[i]

        else:
            mini=i
            for j in range(i+1,len(data)):
                if data[j] < data[mini]:
                    mini=j
            data[i],data[mini]=data[mini],data[i]

    print('#{}'.format(test+1),end=' ')
    for i in range(10):
        print(data[i] , end=' ')
    print()