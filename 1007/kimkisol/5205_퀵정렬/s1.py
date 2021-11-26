import sys

sys.stdin = open('input.txt')


def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)
    return arr

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(t, quick_sort(arr, 0, len(arr)-1)[N//2]))