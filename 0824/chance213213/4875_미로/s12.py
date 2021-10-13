import sys
sys.stdin = open('input.txt')
#visit 따로 안만들고 data에다가 표시함
#근데 이렇게 하면 원본 변경 안되낭?
#여긴 가봤던 길 그냥 나 여기 왔다 갔다 체크해주면 됨. 원본으로 바꿀 필요 X
#왔던 길 되돌아오면서 다른 방향 가볼 때, 앞으로 새로 가볼 곳만 visited 체크하면 됨
def dfs(r, c):
    global ans
    data[r][c] = 'visit' #??
    for k in range(4):
        if ans:
            return
        nr, nc = r + dr[k], c + dc[k]
        if nr < 0 or nr == N: continue  # 범위 체크
        if nc < 0 or nc == N: continue
        if data[nr][nc] == 'visit': continue  # 방문 했던 곳 체크
        if data[nr][nc] == 1: continue  # 벽 체크
        if data[nr][nc] == 3:  # 도착지면
            ans = 1  # 1로 바꾸고 종료
            return
        dfs(nr, nc)


def find_start(data, N):        # 시작지점이 항상 최하단은 아님(tc 3번)
    for r in range(N):          # 미로의 크기만큼 반복을 돌면서
        for c in range(N):
            if data[r][c] == 2: # 2(출발점)을 찾아
                return r, c

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    ans = 0
    sr, sc = find_start(data, N)
    dfs(sr, sc)  # 만약 모든 3을 만나지 못하면 ans의 값은 초기값 0인 상태로 반환
    print('#{} {}'.format(tc, ans))