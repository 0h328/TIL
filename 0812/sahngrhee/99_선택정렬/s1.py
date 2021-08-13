import sys
sys.stdin = open('input.txt')

def selection_sort(nums):
    for i in range(0, len(nums)-1):
        my_min = i
        for j in range(i+1, len(nums)):
            if nums[my_min] > nums[j]:
                my_min = j
        nums[i], nums[my_min] = nums[my_min], nums[i]
    return nums

numbers = list(map(int, input().split()))
print(selection_sort(numbers))