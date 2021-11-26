import sys

N = int(sys.stdin.readline().strip())

a = []

for i in range(N):
    x = list(map(int,sys.stdin.readline().split()))
    a.append(x)


sorted_a = sorted(a)

for m in sorted_a:
    print(*m)