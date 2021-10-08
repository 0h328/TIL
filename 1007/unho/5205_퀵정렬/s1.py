import sys
sys.stdin = open('input.txt')


def partition(arr, start, end):
    left = start + 1
    right = end

    while left <= right:
        while left <= right and arr[left] <= arr[start]:
            left += 1
        while left <= right and arr[start] <= arr[right]:
            right -= 1
        
        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[right], arr[start] = arr[start], arr[right]
    return right


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)
    return arr


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    sorted_li = quick_sort(li, 0, len(li)-1)

    print('#{} {}'.format(tc, sorted_li[N//2]))