import sys
sys.stdin = open('input.txt')

def binary_search(N):

    start = 0
    end = len(list_a) - 1

    if N <= list_a[(start + end)//2]:
        Flag = 'right'
    else:
        Flag = 'left'

    while start <= end:
        mid = (start + end) // 2
        if N == list_a[mid]:
            return True
        elif N < list_a[mid] and Flag == 'right':
            Flag = 'left'
            end = mid - 1
        elif N > list_a[mid] and Flag == 'left':
            Flag = 'right'
            start = mid + 1
        else:
            return False
    return False

T = int(input())

for case in range(T):
    N, M = map(int,input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    list_a = sorted(list_a)
    ans = 0
    for i in list_b:
        if binary_search(i):
            ans += 1
    print('#{} {}'.format(case + 1, ans))