import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))

sum = [nums[0]]
for i in range(len(nums) - 1):
    sum.append(max(sum[i] + nums[i + 1], nums[i + 1]))

print(max(sum))