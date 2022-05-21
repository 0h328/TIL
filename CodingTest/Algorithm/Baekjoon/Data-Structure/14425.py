import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
S = set([input() for _ in range(N)])
ans = 0

for _ in range(M):
    word = input()
    if word in S:
        ans += 1

print(ans)

