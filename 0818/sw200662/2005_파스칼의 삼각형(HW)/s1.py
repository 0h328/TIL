import sys

sys.stdin = open('input.txt')

T = int(input())
list1 = []
list2 = []
for i in range(T):
    print('#{}'.format(i+1))
    k = int(input())
    for a in range(0, k):
        list1 = list2[::]
        list2 = [1] * (a+1)
        if a == 0 or a == 1:
            for k in list2:
                print(k,end=' ')
            print()
        else:
            for c in range(1,a):
                list2[c] = list1[c-1] + list1[c]
            for z in list2:
                print(z,end=' ')
            print()