import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))

while True:
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            print(*nums)
    if nums == sorted(nums):
        break
