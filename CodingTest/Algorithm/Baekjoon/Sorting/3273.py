import sys
sys.stdin = open('input.txt')

n = int(input())
nums = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())

ans = 0
left, right = 0, n-1 # 왼쪽, 오른쪽
while left < right:
    temp = nums[left] + nums[right]
    if temp == x:
        ans += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1

print(ans)