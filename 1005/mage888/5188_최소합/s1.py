import sys
sys.stdin = open('input.txt')

def dfs(r, c, total):
    global ans  # 계속 업데이트하기 때문에 global 선언

    # 종료조건
    if r == N-1 and c == N-1:   # 오른쪽 아래에 도착했을경우
        if ans > total:         # 숫자의 합이 지금까지 움직인 경로의 합보다 작은 경우
            ans = total         # 업데이트
        return

    elif ans < total:           # 도착하지도 않았는데, 기존 설정한 최댓값보다 클 경우
        return                  # 바로 종료

    dr, dc = [0, 1], [1, 0]     # 오른쪽, 아래로만 이동

    for i in range(2):
        nr = r + dr[i]          # 움직인 위치
        nc = c + dc[i]

        if nr < N and nc < N:   # arr 리스트의 범위 내에만 이동
            dfs(nr, nc, total + arr[nr][nc])    # 처음 위치에서부터 계속 더해줌


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 10*N*N    # 숫자의 합계를 최대로 선언

    dfs(0, 0, arr[0][0])

    print('#{} {}'.format(tc, ans))

