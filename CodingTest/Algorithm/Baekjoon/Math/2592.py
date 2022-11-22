import sys
sys.stdin = open('input.txt')

nums = [int(input()) for i in range(10)]
print(sum(nums)//10)
print(max(nums, key=nums.count))