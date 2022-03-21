import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))
nums.sort()
print(nums[1])