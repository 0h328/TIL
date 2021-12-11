import sys
input = sys.stdin.readline

c, r = map(int, input().split())
N = int(input())
cut = []
for _ in range(N):
    cut.append(list(map(int, input().split())))

width, height = [0, c], [0, r]
for i in range(len(cut)):
    if cut[i][0]:
        width.append(cut[i][1])
    else:
        height.append(cut[i][1])

width.sort()
height.sort()

r_max = 0
for i in range(1, len(width)):
    if r_max < width[i]-width[i-1]:
        r_max = width[i]-width[i-1]

c_max = 0
for i in range(1, len(height)):
    if c_max < height[i]-height[i-1]:
        c_max = height[i]-height[i-1]

print(r_max*c_max)



