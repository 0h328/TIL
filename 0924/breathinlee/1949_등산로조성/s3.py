import sys
sys.stdin = open('input.txt')

# 라이브 강의 풀이(현재 위치를 들고 다닐 때)
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def work2(r, c, h, road, skill):
    global ans
    if road > ans:
        ans = road
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]:
            continue
        if h > mountain[nr][nc]:
            work2(nr, nc, mountain[nr][nc], road + 1, skill)
        elif skill and h > mountain[nr][nc] - K:
            work2(nr, nc, mountain[r][c] - 1, road + 1, 0)  # mountain[r][c] - 1 내 다음 좌표의 높이 / skill 사용처리 => 0

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
                work2(i, j, max_height, 1, 1)

    print('#{} {}'.format(tc, ans))