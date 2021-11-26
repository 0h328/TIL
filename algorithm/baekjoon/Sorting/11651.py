import sys

N = int(sys.stdin.readline().strip())

a = []

for _ in range(N):
    x, y = list(map(int,sys.stdin.readline().split()))
    a.append([y,x])

sorted_a = sorted(a)

for x, y in sorted_a:
    print(y, x)