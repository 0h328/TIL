import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

nums = list(map(int, input().split()))
cnt = 0

for i in range(1<<len(nums)):
    for j in range(len(nums)):
        if i & (1<<j):
            print(nums[j], end=' ')
    print()
    cnt += 1

print(cnt)