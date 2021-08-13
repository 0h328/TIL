import sys
sys.stdin = open('input.txt')


def selection_sort(nums):

    for k in range(len(nums)):
        mini = nums[k]
        for idx in range(k, len(nums)):
            if nums[idx] <= mini: #같은 숫자인 경우
                mini = nums[idx]
                min_idx = idx
        nums[k], nums[min_idx] = nums[min_idx], nums[k]
    return nums

nums = list(map(int, input().split()))
print(selection_sort(nums))