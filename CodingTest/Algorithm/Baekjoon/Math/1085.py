import sys
sys.stdin = open('input.txt')

x, y, w, h = map(int, input().split())

min_dist = []
min_dist.append(abs(0-x))
min_dist.append(abs(0-y))
min_dist.append(abs(w-x))
min_dist.append(abs(h-y))

print(min(min_dist))
