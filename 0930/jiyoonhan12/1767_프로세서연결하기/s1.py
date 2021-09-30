import sys
sys.stdin = open('input.txt')

'''
아직 안끝남!!!
'''

# 상우하좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, 1]

def fill(i, j, k):
    global visited
    while 0 <= i < N and 0 <= j < N and not visited[i][j]:
        visited[i][j] = 2
        i += di[k]
        j += dj[k]
    if i != 0 and i != N-1 and j != 0 and j != N-1:
        delete(i, j, (k+2)%4)

def delete(i, j, k):
    global visited
    while 0 <= i < N and 0 <= j < N and visited[i][j] == 2:
        visited[i][j] = 0
        i += di[k]
        j += dj[k]


def dfs(idx):
    global visited, ans
    cnt = 0
    if idx > len(core):
        for r in range(N):
            for c in range(N):
                if visited[r][c] == 2:
                    cnt += 1
        if cnt < ans:
            ans = cnt
    i, j = core[idx]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 < i < N-1 and 0 < j < N-1 and 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            fill(i, j, k)
            dfs(idx+1)
            delete(i, j, (k+2)%4)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    ans = 144

    core = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                visited[i][j] = 1
                core.append((i, j))

    dfs(0)
    print(ans)