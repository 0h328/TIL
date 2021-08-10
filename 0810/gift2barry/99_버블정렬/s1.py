import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split(', ')))

# for i in range(0, len(nums)-1):
#     for j in range(0, len(nums)-i-1):
#         if nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]
# print(nums)

for i in range(len(nums)-1, 0, -1):

    for j in range(i):
        