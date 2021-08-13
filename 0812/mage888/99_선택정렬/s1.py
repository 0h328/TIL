def selection_sort(nums):

    for i in range(len(nums)-1):
        minimum = i
        for j in range(i+1, len(nums)):
            if nums[minimum] > nums[j]:
                minimum = j
        nums[i], nums[minimum] = nums[minimum], nums[i]

    return nums

import sys
sys.stdin = open('input.txt')

numbers = list(map(int, input().split()))
print(numbers)
print(selection_sort(numbers))