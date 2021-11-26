def quicksort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]
    less = []
    more = []
    equal = []
    for a in nums:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quicksort(less) + equal + quicksort(more)


import sys
sys.stdin = open('input.txt')
nums = list(map(int, input().split()))
print(quicksort(nums))