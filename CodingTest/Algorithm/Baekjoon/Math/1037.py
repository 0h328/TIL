import sys
sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))
print(min(nums)*max(nums))