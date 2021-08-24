def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[0]
    tail = nums[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


# 가변 배열
import sys

sys.stdin = open('input.txt')
nums = list(map(int, input().split()))
print(quick_sort(nums))
