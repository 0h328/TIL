import sys
sys.stdin = open('input.txt')

def partition(numbers, start, end):
    pivot = numbers[start]
    left = start + 1
    right = end
    ans = False
    while not ans:
        while left <= right and numbers[left] <= pivot:
            left += 1
        while left <= right and pivot <= numbers[right]:
            right -= 1
        if right < left:
            ans = True
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]
    numbers[start], numbers[right] = numbers[right], numbers[start]
    return right

def quick_sort(numbers, start, end):
    if start < end:
        pivot = partition(numbers, start, end)
        quick_sort(numbers, start, pivot-1)
        quick_sort(numbers, pivot+1, end)
    return numbers


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    A = quick_sort(numbers, 0, len(numbers)-1)
    print('#{} {}'.format(tc, A[N//2]))
