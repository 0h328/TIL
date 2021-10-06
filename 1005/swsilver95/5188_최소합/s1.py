import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

dx = [0, 1]                                             # 우, 하 / 위쪽과 왼쪽은 고려할 필요가 없음
dy = [1, 0]


def dfs(row, col, total):                               # 1. dfs 탐색 함수 / 시작점, 현재까지의 합을 인자로 가지고 있음
    global answer
    if answer < total:                                  # 4. 만약 현재까지 나온 정답보다 이미 total값이 크다면
        return                                          # 4.1. 더 탐색할 필요가 없다.

    if row == N - 1 and col == N - 1:                   # 5. 오른쪽 아래 지점에 도달했다면,
        if answer > total:                              # 5.1. total과 answer를 비교하여 더 작은 쪽으로 갱신
            answer = total

    for r in range(2):                                  # 2. 오른쪽과 아래쪽 두 방향에 대해서
        nx = row + dx[r]                                # 2.1. 각 방향으로 이동한 좌표를 지정해주고
        ny = col + dy[r]
        if 0 <= nx < N and 0 <= ny < N:                 # 3. 각 방향이 이동 가능한 격자 내에 있고
            if not visited[nx][ny]:                     # 3.1. 방문하지 않았다면
                visited[nx][ny] = True                  # 3.2. 방문처리를 한 다음
                dfs(nx, ny, total + data[nx][ny])       # 3.3. 해당 지점을 시작점으로 다시 dfs 탐색 / 이 때 지금까지의 합에 방금 위치의 숫자를 인자로 더해줌
                visited[nx][ny] = False                 # 3.4. 다시 방문처리를 취소


for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]   # 방문 처리 이차원배열
    visited[0][0] = True                        # 시작 지점은 왼쪽 위로 고정되어 있으므로 방문 처리
    answer = 1001                               # 정답은 1000 이하의 숫자
    dfs(0, 0, data[0][0])                       # dfs 탐색 시작
    print('#{} {}'.format(tc, answer))
