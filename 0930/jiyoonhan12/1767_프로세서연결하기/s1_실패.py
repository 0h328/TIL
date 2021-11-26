import sys
sys.stdin = open('input.txt')

'''
아직 안끝남!!!
'''

# 상우하좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, 1]

def fill(i, j, k):
    global visited, cnt_link
    while 0 <= i < N and 0 <= j < N and not visited[i][j]:
        visited[i][j] = 2
        i += di[k]
        j += dj[k]
    if i != 0 and i != N-1 and j != 0 and j != N-1: # 중간에 끊겼을 때
        i -= di[k]
        j -= dj[k]
        delete(i, j, (k+2)%4)
    if i == 0 or i == N-1 or j == 0 or j == N-1:
        cnt_link += 1

def delete(i, j, k):
    global visited, cnt_link
    if (i == 0 or i == N-1 or j == 0 or j == N-1) and visited[i][j] == 2:
        cnt_link -= 1
    while 0 <= i < N and 0 <= j < N and visited[i][j] == 2:
        visited[i][j] = 0
        i += di[k]
        j += dj[k]

def dfs(idx):
    global visited, linked, ans, cnt_link
    cnt = 0 # 전선 길이
    if idx >= len(core):
        for r in range(N):
            for c in range(N):
                if visited[r][c] == 2:
                    cnt += 1
        if cnt_link >= linked:
            if cnt_link > linked:
                ans = cnt # 최대값으로 다시 초기화
            if cnt < ans:
                ans = cnt
        return

    i, j = core[idx]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            fill(ni, nj, k)
            dfs(idx+1)
            delete(ni, nj, (k+2)%4)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    linked, cnt_link = 0, 0 # 연결된 core 개수
    ans = 144 # 연결된 선 길이

    core = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                visited[i][j] = 1
                core.append((i, j))

    dfs(0)
    print(ans)