import sys
sys.stdin = open('input.txt')

def selection_sort(nums):
    cur_idx = 0
    while cur_idx < len(nums)-1:
        min_idx = cur_idx
        for i in range(cur_idx + 1, len(nums)):
            if nums[i] < nums[min_idx]:
                min_idx = i
        nums[cur_idx], nums[min_idx] = nums[min_idx], nums[cur_idx]
        cur_idx += 1
    return nums

numbers = list(map(int, input().split()))
print(numbers)
print(selection_sort(numbers))