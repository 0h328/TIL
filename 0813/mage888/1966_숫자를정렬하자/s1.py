import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int,input().split()))

    for i in range(len(a)-1):
        min_num = i
        for j in range(i+1, len(a)):
            if a[min_num] > a[j]:
                min_num = j
        a[i], a[min_num] = a[min_num], a[i]

    print('#{}'.format(tc), end=' ')
    print(*a)


