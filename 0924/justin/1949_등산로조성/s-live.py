import sys
sys.stdin = open('input.txt')
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 1. 현재 위치를 들고 다니지 않을때
# r,c 좌표, road는 지금까지 조성된 등산로의 길이, skill 공사 유무
def work(r, c, road, skill):
    global ans
    if road > ans: ans = road

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            # a.현위치보다 낮은곳으로 이동할 때.
            if mountain[r][c] > mountain[nr][nc]:
                work(nr, nc, road + 1, skill)
            # b.현위치보다 높거나 같은 곳으로 이동할 때
            elif skill and mountain[r][c] > mountain[nr][nc] - K:
                tmp = mountain[nr][nc]  # 기록
                mountain[nr][nc] = mountain[r][c] - 1
                work(nr, nc, road + 1, 0)  # 스킬 사용
                mountain[nr][nc] = tmp  # 원상복구

    visited[r][c] = 0


# 2. 현재위치를 들고다니자...
def work2(r, c, h, road, skill):
    global ans
    if road > ans: ans = road
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]: continue

        if h > mountain[nr][nc]:
            work2(nr, nc, mountain[nr][nc], road + 1, skill)
        elif skill and h > mountain[nr][nc] - K:
            work2(nr, nc, mountain[r][c] - 1, road + 1, 0)

    visited[r][c] = 0


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N : 한변의 길이, K: 최대 공사가 가능한 깊이

    # N*N 크기의 2차원 리스트(배열)이 주어진다.

    mountain = [list(map(int, input().split())) for _ in range(N)]
    max_h = 0

    # 최고 높이의 봉우리를 찾는 과정
    for i in range(N):
        for j in range(N):
            if max_h < mountain[i][j]:
                max_h = mountain[i][j]

    # mountain = []
    # max_h = 0
    # for i in range(N):
    #     #한줄 입력을 받고 내부에서 가장 큰값을 찾자
    #     tmp = list(map(int, input().split()))
    #
    #     for j in tmp:
    #         if max_h < j:
    #             max_h = j
    #
    #     mountain.append(tmp)

    visited = [[0] * N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_h:
                # work(i, j, 1, 1)  # 좌표, 길, 스킬
                work2(i, j, max_h, 1, 1) #좌표, 높이, 길, 스킬

    print("#{} {}".format(tc, ans))
