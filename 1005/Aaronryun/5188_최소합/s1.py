import sys

sys.stdin = open('input.txt')


def dfs(x, y, temp):
    global answer
    if x == N - 1 and y == N - 1:  # 목표 지점 도착하면
        if temp < answer:  # 최소값 갱신
            answer = temp
        return
    if temp > answer: # 더 큰 경우는 볼 필요가 없음
        return

    for i in range(2): # 두방향
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0: #범위안에
            visited[nx][ny] = 1
            dfs(nx, ny, temp + data[nx][ny])
            visited[nx][ny] = 0 # 방문지 초기화


for test in range(1, 1 + int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    dx = [0, 1]
    dy = [1, 0]
    answer = 1e9
    visited[0][0] = 1
    dfs(0, 0, data[0][0])
    print('#{} {}'.format(test, answer))
