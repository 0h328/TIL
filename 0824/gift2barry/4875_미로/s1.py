import sys
sys.stdin = open('input.txt')

# thought process:
# 머리로는 이해 x
# 일단은 따라풀어보며 코드를 바꿔보며 왜 틀렸는지 생각하며 공부

def dfs(r, c):
    global ans
    for i in range(4):                         # 각 idx 마다 4방 체크, 갈 수 있는곳 확인
        nr, nc = r + dr[i], c + dc[i]            # potential 이동위치 배정

        if 0 <= nr < N and 0 <= nc < N:        # 탐색 범위 미로 내로 지정
            if arr[nr][nc] == 3:               # 이동하고 탈출구 발견하면 바로 끝
                ans = 1
                return
                # return 1      # 왜 이건 안될까?
            if not arr[nr][nc] and not v[nr][nc]:  # 통로가 있고, 아직 방문 안했으면,
                v[nr][nc] = 1                          # 방문체크 하고
                dfs(nr, nc)                            # 탐색하러 ㄱ

for tc in range(1, int(input())+1):

    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
        #  상 우 하 좌
    dr = [-1, 0, 1, 0]                      # 방향 델타값 생성
    dc = [0, 1, 0, -1]

    v = [[0] * N for _ in range(N)]         # visited 체크 리스트 생성
    ans = 0                                 # 정답 생성

    x, y = 0, 0
    for i in range(N):                      # 시작지점 찾기
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j                 # 찾으면 인덱스 위치 변수에 할당,
                break
    dfs(x, y)
    print('#{} {}'.format(tc, ans))
    # print('#{} {}'.format(tc, dfs(x, y)))  왜 이건 안될까?



