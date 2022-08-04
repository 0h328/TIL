import sys
from itertools import combinations
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))

f = []
for i in range(1, N+1):
    f.append(combinations(arr, i))

ans = 1000000000
for i in f:
    for e in i:
        sour = 1
        bitter = 0
        for j in e:
            sour *= j[0]
            bitter += j[1]

        ans = min(ans, abs(sour - bitter))

print(ans)