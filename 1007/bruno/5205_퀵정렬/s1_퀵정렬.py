import sys
sys.stdin = open('input.txt')


def partition(lst, l, r):
    p = lst[l]
    i = l
    j = r
    while i < j:
        while i <= j and lst[i] <= p:
            i += 1
        while i <= j and lst[j] >= p:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j] = lst[j], lst[l]
    return j


def quicksort(lst, l, r):
    if l < r:
        s = partition(lst, l, r)
        quicksort(lst, l, s - 1)
        quicksort(lst, s + 1, r)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    quicksort(A, 0, N-1)
    print('#{} {}'.format(tc, A[N//2]))
