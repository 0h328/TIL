import sys
sys.stdin = open('input.txt')

for m in range(10):
    Try = int(input())
    nums = list(map(int,input().split()))

    while cnt:
        max_height = min_height = nums[0]
        max_idx = min_idx = 0