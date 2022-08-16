import sys
sys.stdin = open('input.txt')

L = int(input())
nums = list(map(int, input().split()))
target = int(input())

nums.append(0)
nums.sort()

A = 0
for i in range(len(nums)-1) :
    if nums[i] == target or nums[i+1] == target:
        A = 0
        break
    elif nums[i] < target and target < nums[i+1]:
        A = (target - nums[i]) * (nums[i+1] - target) - 1
        break

print(A)