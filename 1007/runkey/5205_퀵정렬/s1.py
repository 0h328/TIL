import sys
sys.stdin = open('input.txt')

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, equal, right = [], [], []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    return quick_sort(left) + equal + quick_sort(right)

tc = int(input())

for t in range(1, tc + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = quick_sort(arr)
    result = arr[N//2]
    print("#{} {}".format(t, result))