import sys
sys.stdin = open('input.txt')


def partition(arr, start, end):
    p = arr[start]
    L = start + 1
    R = end
    while True:
        while L <= R and arr[L] <= p:
            L += 1
        while L <= R and p <= arr[R]:
            R -= 1
        if R < L:
            break
        else:
            arr[L], arr[R] = arr[R], arr[L]
    arr[start], arr[R] = arr[R], arr[start]
    return R


def quicksort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        quicksort(arr, start, p-1)
        quicksort(arr, p+1, end)
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    quicksort(num, 0, N-1)
    print('#{} {}'.format(tc, num[N//2]))