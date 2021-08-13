import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

numbers = list(map(int, input().split()))
print(selection_sort(numbers))