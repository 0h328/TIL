import sys
sys.stdin = open("input.txt")


nums = list(map(int, input().split()))
# 내림차순
"""
for i in range(len(nums)-1, 0, -1):
    for j in range(i):
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
"""
# print(nums)

# 오름차순
for i in range(len(nums)-1, 0, -1):
    for j in range(i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(*nums)