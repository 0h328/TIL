import sys
sys.stdin = open('input.txt')

def selection_sort(nums):
    for i in range(len(nums)-1):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

numbers = list(map(int, input().split()))
print(numbers)
print(selection_sort(numbers))