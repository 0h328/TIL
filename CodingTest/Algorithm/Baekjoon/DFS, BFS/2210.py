import sys
sys.stdin = open('input.txt')

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c, case):

    if len(case) == 6:
        res.add(case)
        return  # return을 통해 백트래킹 가능

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, case+arr[nr][nc])   # return을 통해 백트래킹 가능

arr = [list(input().split()) for _ in range(5)]
v = [[0] * 5 for _ in range(5)]
res = set() # 중복을 제거하기 위해 set

for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])    # 시작좌표와 시작인자를 변수로 추가

print(len(res))