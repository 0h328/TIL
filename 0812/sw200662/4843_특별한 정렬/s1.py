import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N = int(input())
    list1 = list(map(int,input().split()))
    list1.sort()
    check = 0
    cnt = 0
    print('#{}'.format(i+1),end=' ')
    while len(list1) >= 1 and cnt != 10:
        print(list1.pop(),end=' ')
        cnt +=1
        if check == 0:
            list1.sort(reverse=True)
            check = 1
        else:
            list1.sort()
            check = 0
    print()