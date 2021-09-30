import sys
sys.stdin = open('input.txt')

# 라이브 강의 풀이(현재 위치를 들고 다니지 않을 때)  => 원상복구 작업이 필요함
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# r, c : 좌표 / road는 지금까지 조성된 등산로의 길이 / skill은 공사 유무
def work(r, c, road, skill):
    global ans
    if road > ans:
        ans = road

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            # a. 현 위치보다 낮은 곳으로 이동할 때,
            if mountain[r][c] > mountain[nr][nc]:
                work(nr, nc, road + 1, skill)
            # b. 현 위치보다 높거나 같은 곳으로 이동할 때,
            elif skill and mountain[r][c] > mountain[nr][nc] - K:
                tmp = mountain[nr][nc]  # 기록
                mountain[nr][nc] = mountain[r][c] - 1
                work(nr, nc, road + 1, 0)  # 스킬 사용
                mountain[nr][nc] = tmp  # 원상 복구

    visited[r][c] = 0


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split()) # N : 한 변의 길이, K : 최대 공사가 가능한 깊이

    mountain = [list(map(int, input().split())) for _ in range(N)]
    max_height = 0

    for i in range(N):
        for j in range(N):
            if max_height < mountain[i][j]:
                max_height = mountain[i][j]


    visited = [[0] * N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_height:
                work(i, j, 1, 1)

    print('#{} {}'.format(tc, ans))
