import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
left, right = 0, len(nums) - 1
cnt = 0

while left < right:
    sum_num = nums[left] + nums[right]
    if sum_num < m:
        left += 1
    elif sum_num > m:
        right -= 1
    else:
        cnt += 1
        left += 1
        right -= 1

print(cnt)