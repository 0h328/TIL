import sys
sys.stdin = open('input.txt')
#2. 현재 위치 들고 다니지 않을 때

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def work(r, c, road, skill):
    #road = 지금까지 조성된 등산로 길이, skill= 공사 했는지
    global ans
    if road > ans :
        ans = road
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            #높은 곳에서 낮은 곳으로 가서, visited는 굳이 필요 없긴 함
            #현위치 보다 낮은곳으로 이동 시
            if mountain[r][c] > mountain[nr][nc]:
                work(nr, nc, road+1, skill)
            #현위치 보다 높거나 같은 곳으로 이동 시
            elif skill and mountain[r][c] > mountain[nr][nc] - K:
                tmp = mountain[nr][nc] # just 기록
                mountain[nr][nc] = mountain[r][c] - 1
                work(nr, nc, road+1, 0) #스킬 사용함
                mountain[nr][nc] = tmp #원상복구 ?? 여기 모르겠다.
        visited[r][c] = 0

#3 현재 위치 있는 경우
def work2(r, c, h, road, skill):
    global ans
    if road > ans: ans = road
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0~





T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    max_h = 0

    for i in range(N):
        for j in range(N):
            if max_h < mountain[i][j]:
                max_h = mountain[i][j]

    # mountain = []
    # for i in range(N):
    #     tmp = list(map(int, input().split()))
    #
    #     for j in tmp:
    #         if max_h < j:
    #             max_h = j
    #     mountain.append(tmp)

    visited = [[0] * N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_h:
                work(i, j, 1, 1)

    print('#{} {}'.format(tc, ans))
