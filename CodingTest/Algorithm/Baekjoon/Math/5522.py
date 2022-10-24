import sys
sys.stdin = open('input.txt')

ans = 0
for _ in range(5):
    ans += int(input())

print(ans)