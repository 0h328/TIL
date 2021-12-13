# 통계학
import sys
import statistics
from collections import Counter
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()
print(round(statistics.mean(nums)))
print(statistics.median(nums))

counter = Counter(nums)
cnt = counter.most_common()
if len(nums) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(nums[-1]-nums[0])

