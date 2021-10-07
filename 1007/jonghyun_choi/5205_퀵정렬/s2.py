import sys
sys.stdin = open('input.txt')

def partition(data, start, end):
    pivot = data[start]
    left = start + 1
    right = end
    Flag = False
    while not Flag:
        while left <= right and data[left] < pivot:
            left += 1
        while left <= right and pivot <= data[right]:
            right -= 1
        if right < left:
            Flag = True
        else:
            data[left], data[right] = data[right], data[left]
    data[start], data[right] = data[right], data[start]
    return right

def quicksort(data, start, end):
    if start < end:
        pivot = partition(data, start, end)
        quicksort(data, start, pivot - 1)
        quicksort(data, pivot + 1, end)
    return data


T = int(input())

for case in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    print('#{} {}'.format(case + 1,quicksort(data, 0, len(data) - 1)[N//2]))