import sys
sys.stdin = open('input.txt')

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    sign = True
    while sign:
        while left <= right and pivot >= arr[left]:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1

        if right < left:
            sign = False
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quicksort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot+1, end)
    return arr

nums = list(map(int, input().split()))
print(quicksort(nums, 0, len(nums)-1))




'''
def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)
    return arr

nums = list(map(int, input().split()))
print(quick_sort(nums, 0, len(nums)-1))
'''