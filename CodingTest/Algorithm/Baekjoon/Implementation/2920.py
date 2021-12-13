import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))
rv_nums = sorted(nums)

if nums == rv_nums:
    print('ascending')
elif nums == sorted(rv_nums, reverse=True):
    print('descending')
else:
    print('mixed')