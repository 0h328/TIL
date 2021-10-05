import sys
sys.stdin = open('input.txt')

dx = [1, 0] # 어차피 우랑 하만 가니까
dy = [0, 1]

def dfs(x, y):
    global result, start

    if result < start: # 현재 결과값보다 더 크면 의미가 없으니까 '통과' 시켜버리려고 넣은거
        return

    if x == N-1 and y == N-1: # x, y가 마지막에 도착했을 때
        if start < result:
            result = start
        return

    for i in range(2): # 우, 하 두 방향으로 반복문 돌리기
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < N and ny < N and visited[nx][ny] == 0:
            visited[nx][ny] = 1 # 방문했다고 표시하기
            start += number_map[nx][ny] # 도착한 곳의 해당 값을 start 값에 더해주기
            dfs(nx, ny) # 재귀 방식으로 계속 들어간다.
            visited[nx][ny] = 0 # 재귀 갔다가 나오면서 visited에 1 적어준거 다시 원상복구
            start -= number_map[nx][ny] # 물론 start 값도 빼준다

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number_map = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    start = number_map[0][0]
    result = 100000000
    dfs(0, 0) # dfs를 돌리고 난 후 result 값을 출력해야하니깡
    print('#{} {}'.format(tc, result)) # 값 출력!
