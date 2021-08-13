# input 데이터를 불러온다.
import sys
sys.stdin = open('input.txt')


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

r_ow = 1
c_ol = 1

# drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# for r_ow, c_ol in drc:
#     print(r_ow, c_ol)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for i in range(4):
    nr = r_ow + dr[i]
    nc = c_ol + dc[i]

    if (0 <= nr < n) and (0 <= nc < n):
        print(data[nr][nc])
    if nr < 0 or  nr >= n or nc < 0 or nc >= n:
        continue