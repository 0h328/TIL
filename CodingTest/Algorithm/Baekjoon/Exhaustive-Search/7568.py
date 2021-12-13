import sys
sys.stdin = open('input.txt')

N = int(input())
info = []
for _ in range(N):
    x, y = map(int, input().split())
    info.append([x, y])

for a in info:
    rank = 1
    for b in info:
        if a[0] < b[0] and a[1] < b[1]:
            rank += 1
    print(rank)
