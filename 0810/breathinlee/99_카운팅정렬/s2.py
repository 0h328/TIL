import sys
sys.stdin = open("input.txt")

nums = list(map(int, input().split()))
cnt_nums = [0] * (max(nums) - min(nums) + 1)

for num in nums:
    cnt_nums[num - min(nums)] += 1

# print(cnt_nums)

ans = []
for idx in range(len(cnt_nums)):
    ans += [idx + min(nums)] * cnt_nums[idx]

print(ans)