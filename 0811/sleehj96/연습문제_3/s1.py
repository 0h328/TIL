import sys

sys.stdin = open('input.txt')

# ingredients = ['egg', 'cheeze', 'rice']

# N = len(ingredients)

nums = list(map(int, input().split()))
N = len(nums)

for i in range(1, 1 << N):
    for j in range(N):
        if i & (1 << j):
            print(nums[j], end=' ')
    print()
