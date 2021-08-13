import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

r, c = 1, 1
d = [(-1,0), (1,0), (0,-1), (0,1)]

for dr, dc in d:
    nr, nc = r+dr, c+dc
    print(arr[nr][nc])
# 2
# 8
# 4
# 6