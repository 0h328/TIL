import sys
sys.stdin = open('input.txt')

N = int(input())
tmp = 0
ans = 0
res = list(map(int, input().split()))

for i in range(N):
    if res[i] == 1:
        tmp += 1
        ans += tmp
    else:
        tmp = 0

print(ans)