import sys
sys.stdin = open('input.txt')

X = int(input())

s = [64, 32, 16, 8, 4, 2, 1]
ans = 0

for i in range(len(s)):
    if X >= s[i]:
        ans += 1
        X -= s[i]

print(ans)