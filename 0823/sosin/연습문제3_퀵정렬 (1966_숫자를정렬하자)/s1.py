def quick_sort(nums):
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

    return quick_sort(less) + equal + quick_sort(more)

# 가변 배열
import sys
sys.stdin = open('input.txt')
nums = list(map(int, input().split()))
print(quick_sort(nums))