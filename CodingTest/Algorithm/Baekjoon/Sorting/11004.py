import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

print(nums[K-1])