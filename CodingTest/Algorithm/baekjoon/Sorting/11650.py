import sys

N = int(sys.stdin.readline().strip())

a = [] 

for i in range(N):
    x, y = list(map(int,sys.stdin.readline().split()))
    a.append([x, y])
print(a)

sorted_a = sorted(a)

for m, n in sorted_a:
    print(m, n)

