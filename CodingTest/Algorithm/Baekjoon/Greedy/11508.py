import sys
sys.stdin = open('input.txt')

N = int(input())
c = []
for i in range(N):
  c.append(int(input()))
c.sort(reverse=True)

res=0
for i in range(2, len(c), 3):
  res += c[i]

print(sum(c)-res)