import sys
sys.stdin = open('input.txt')


Numbers = list(map(int, input().split()))
print(Numbers)

def selection_sort(nums):

    M = len(nums)

    for i in range(M-1):
        min_idx = i
        for j in range(i + 1, M):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

print(selection_sort(Numbers))