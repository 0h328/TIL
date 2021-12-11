import sys
sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input()))

print(sum(nums))