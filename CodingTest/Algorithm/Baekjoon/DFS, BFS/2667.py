#단지번호붙이기
import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    global cnt
    arr[r][c] = 0
    cnt += 1
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
            dfs(nr, nc)
    

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
tmp = []
cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            dfs(i, j)
            tmp.append(cnt)
            cnt = 0

print(len(tmp))
tmp.sort()
for num in tmp:
    print(num)