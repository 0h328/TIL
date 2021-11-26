import sys
sys.stdin = open('input.txt')

T = int(input())

for k in range(T):
    N, K = map(int,input().split())
    list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
    cnt = 0 # 몇
    lst = []
    for i in range(1 << len(list1)):
        a = []
        for j in range(1 << len(list1)):
            if i & (1 << j):
                a.append(list1[j])
        lst.append(a)

    len_lst = []
    for i in lst:
        if len(i) == N:
            len_lst.append(i)
    for i in len_lst:
        if sum(i) == K:
            cnt +=1
    print('#{} {}'.format(k+1,cnt))