import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))

ans = 0
for num in nums:
    ans += num**2

print(ans%10)