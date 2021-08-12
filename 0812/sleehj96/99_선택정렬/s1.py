import sys
sys.stdin = open('input.txt')


def selection_sort(nums):
    n = len(nums)
    for i in range(n-1):
        min_idx = i
        for j in range(i, n):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums

numbers = list(map(int, input().split()))
print(selection_sort(numbers))