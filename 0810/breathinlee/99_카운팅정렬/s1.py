import sys
sys.stdin = open('input.txt')

data = list(map(int, input().split()))
cnt_nums = [0] * (max(data) - min(data) + 1)   # 음수 고려한 리스트 생성

for num in data:
    cnt_nums[num - min(data)] += 1

# print(cnt_nums)

ans = []

for idx in range(len(cnt_nums)):
    ans += [idx + min(data)] * cnt_nums[idx]    # 예) [-1] * 2 이면 [-1, -1]이 들어감.

print(ans)
