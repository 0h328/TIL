import sys

sys.stdin = open('input.txt')

def BubbleSort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

for t in range(10):

    dump = int(input())

    test = list(map(int,input().split()))

    for i in range(dump): # 덤프 수만큼 정렬하면서
        BubbleSort(test)
        test[0]+=1
        test[-1]-=1

    BubbleSort(test)
    answer = test[-1]-test[0]

    print('#{} {}'.format(t+1,answer))