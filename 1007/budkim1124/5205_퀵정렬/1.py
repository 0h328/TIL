import sys
sys.stdin = open("input.txt")

def quick_sort(numbers):
    N = len(numbers)

    if N <= 1:
        return numbers
    pivot = numbers[0]
    left, right = [], []

    for idx in range(1, N):
        if numbers[idx] > pivot:
            right.append(numbers[idx])
        else:
            left.append(numbers[idx])

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)
    return [*sorted_left, pivot, *sorted_right]


T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    result = quick_sort(arr)

    print("#{} {}".format(t+1, result[N//2]))