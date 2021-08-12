import sys
sys.stdin = open('input.txt')

nums = list(map(int,input().split()))

for i in range(1<<len(nums)):
    a = 0
    for j in range(len(nums)):
        if i & (1 << j):
            a += nums[j]
    if a == 0:
        print(1)