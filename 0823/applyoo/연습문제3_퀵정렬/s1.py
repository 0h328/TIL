import sys
sys.stdin = open('input.txt')


def quick_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums)//2

    pivot = nums[0]
    left_nums = [i for i in nums[1:] if i <= pivot]
    right_nums = [i for i in nums[1:] if i > pivot]

    return quick_sort(left_nums) + [pivot] + quick_sort(right_nums)


# 가변 배열
import sys
sys.stdin = open('input.txt')
nums = list(map(int, input().split()))
print(quick_sort(nums))