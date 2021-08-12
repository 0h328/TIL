import sys
sys.stdin = open('input.txt')


def selection_sort(nums):
    for i in range(0, len(nums)-1):
        min_idx = i
        for j in range(i, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


numbers = list(map(int, input().split()))
print(selection_sort(numbers))