import sys
sys.stdin = open('input.txt')

def gcd(x, y):
    while y != 0:
        k = x % y
        x = y
        y = k
    return x

N = int(input())
nums = list(map(int, input().split()))

for i in range(1, N):
    ans = gcd(nums[0], nums[i])
    print('{0}/{1}'.format(nums[0]//ans, nums[i]//ans))