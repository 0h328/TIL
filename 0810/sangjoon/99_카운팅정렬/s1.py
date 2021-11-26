import sys

sys.stdin = open("input.txt")

nums = list(map(int, input().split()))

# 음수 고려한 리스트 생성
max_num, min_num = max(nums), min(nums)
counter = [0] * (max_num - min_num + 1)

for num in nums:
    counter[num - min_num] += 1

ans = []
for idx in range(len(counter)):
    # print("{} ".format(idx + min_num) * counter[idx], end="")
    ans += [idx + min_num] * counter[idx]

print(ans)