import sys
sys.stdin = open("input.txt")

num = int(input())
print(num)

nums = list(map(int, input().split()))
print(nums)

N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]
print(numbers)