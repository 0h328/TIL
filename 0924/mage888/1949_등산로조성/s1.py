import sys
sys.stdin = open('input.txt')

#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#1. 현재 위치를 들고 다니지 않을때
#r,c는 좌표, road는 지금 까지 조성된 등산로의 길이, skill은 공사 유무
def work(r, c, road, skill):
    global ans

    if road > ans:         ans = road

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr in range(N) and nc in range(N) and not visited[nr][nc]:

            #a.현위치보다 낮은곳으로 이동할때
            if m[r][c] > m[nr][nc]:
                work(nr, nc, road+1, skill)
            #b.현위치보다 높거나 같은 곳으로 이동할때
            elif skill and m[r][c] > m[nr][nc] - K:
                tmp = m[nr][nc] #기록
                m[nr][nc] = m[r][c] - 1
                work(nr, nc, road+1, 0) #스킬 사용
                m[nr][nc] = tmp #원상복구

    visited[r][c] = 0

#2. 현재위치를 들고 다닐때
def work2(r, c, h, road, skill):
    global ans
    if road > ans: ans = road
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]: continue
        if h > m[nr][nc]:
            work2(nr, nc, m[nr][nc], road+1, skill)
        elif skill and h > m[nr][nc] - K:
            work2(nr, nc, m[r][c]-1, road+1, 0)

    visited[r][c] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    # N*N 크기의 2차원 리스트(배열)
    m = [list(map(int, input().split())) for _ in range(N)]
    max_height = 0

    for i in range(N):
        for j in range(N):
            if max_height < m[i][j]:
                max_height = m[i][j]

    visited = [[0] * N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if m[i][j] == max_height:
                # work(i, j, 1, 1) #좌표, 길, 스킬
                work2(i, j, max_height, 1, 1) #좌표, 높이, 길, 스킬


    print('#{} {}'.format(tc, ans))


