import sys
sys.stdin = open('input.txt')

ans = []
p = 0

for _ in range(4):
    a, b = map(int, input().split())
    p += b
    p -= a
    ans.append(p)

print(max(ans))