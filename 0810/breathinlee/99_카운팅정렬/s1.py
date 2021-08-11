import sys
sys.stdin = open('input.txt')

data = list(map(int, input().split()))
cnt_nums = [0] * len(data)
for num in data:
    cnt_nums[num] += 1
print(cnt_nums)

