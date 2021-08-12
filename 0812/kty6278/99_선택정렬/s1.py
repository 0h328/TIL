import sys
sys.stdin = open('input.txt')

def selection_sort(nums):
    for i in range(0, len(nums) - 1):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[min] > nums[j]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
    return nums


nums = list(map(int, input().split()))
print(nums)
print(selection_sort(nums))