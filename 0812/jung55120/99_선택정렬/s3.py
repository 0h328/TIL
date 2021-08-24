import sys
sys.stdin = open('input.txt')


def selection_sort(nums):


    for i in range(len(nums)-1):
        min_idx = i
        for j in range(1+i, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[min_idx], nums[j] = nums[j], nums[min_idx]

    return nums

numbers = list(map(int, input().split()))
print(selection_sort(numbers))