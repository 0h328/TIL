import sys
sys.stdin = open('input.txt')

def DFS(i, j, h, check, temp):
    global answer
    visited[i][j] = 1
    if answer < temp:
        answer = temp

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            if h > mountain[ni][nj]:
                DFS(ni, nj, mountain[ni][nj], check, temp+1)
                visited[ni][nj] = 0
            elif check == 1:
                if h > mountain[ni][nj] - K:
                    DFS(ni, nj, h-1, 0, temp+1)
                    visited[ni][nj] = 0


di = [1, 0, -1, 0]  # 시계방향 / 우하좌상
dj = [0, 1, 0, -1]

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    top = 0
    answer = 0
    coor = []
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > top:
                top = mountain[i][j]

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == top:
                coor.append((i, j))
    # print(coor)

    for s in coor:
        i, j = s
        visited = [[0]*N for _ in range(N)]
        DFS(i, j, top, 1, 1)

    print('#{} {}'.format(tc, answer))