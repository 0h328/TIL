import sys
sys.stdin = open('input.txt')

def backtracking(idx, ans, plus, minus, multi, div):
    global max_nums, min_nums

    if idx == N:
        max_nums = max(max_nums, ans)
        min_nums = min(min_nums, ans)
        return

    if plus > 0:
        backtracking(idx+1, ans+nums[idx], plus-1, minus, multi, div)
    if minus > 0:
        backtracking(idx+1, ans-nums[idx], plus, minus-1, multi, div)
    if multi > 0:
        backtracking(idx+1, ans*nums[idx], plus, minus, multi-1, div)
    if div > 0:
        backtracking(idx+1, int(ans/nums[idx]), plus, minus, multi, div-1)

N = int(input())
nums = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())

max_nums = -987654321
min_nums = 987654321

backtracking(1, nums[0], plus, minus, multi, div)

print(max_nums)
print(min_nums)