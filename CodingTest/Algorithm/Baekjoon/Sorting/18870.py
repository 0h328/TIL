import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums_set = sorted(list(set(nums)))  # -10, -9, 2, 4

nums_dict = {nums_set[i] : i for i in range(len(nums_set))}
# {-10: 0, -9: 1, 2: 2, 4: 3}
for num in nums:
    print(nums_dict[num], end=' ')

# 2, 3, 0, 3, 1