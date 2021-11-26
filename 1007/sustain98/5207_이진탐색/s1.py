import sys
sys.stdin = open('input.txt')

def binary_search(x):
    s = 0
    e = n-1
    pre = -1 #0은 왼, 1은 오
    while s <= e:
        mid = (s + e) // 2
        if x == A[mid]:
            return 1
        elif x < A[mid]: #왼
            e = mid - 1
            if pre == 0:
                return 0
            pre = 0
        else: #오
            s = mid + 1
            if pre == 1:
                return 0
            pre = 1
    return 0


t = int(input())
for idx in range(1, t+1):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    res = 0

    for num in B:
        res += binary_search(num)

    print('#{} {}'.format(idx, res))