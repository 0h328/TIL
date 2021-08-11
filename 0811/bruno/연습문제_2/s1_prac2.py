import sys
sys.stdin = open('input.txt')

n = m = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
k = 0
print(arr)
for i in range(n):
    for j in range(m):
        ni, nj = i + di[k], i + dj[k]

