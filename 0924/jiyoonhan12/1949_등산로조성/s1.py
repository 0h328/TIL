import sys
sys.stdin = open('input.txt')

# 라이브 풀이 참고

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(i, j, route, construction):
    global visited, ans

    if route > ans:
        ans = route

    visited[i][j] = 1

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            if arr[i][j] > arr[ni][nj]: # 공사 안 해도 내려갈 수 있다면
                dfs(ni, nj, route + 1, construction)
            elif construction and arr[i][j] > arr[ni][nj] - K: # 공사 해야만 내려갈 수 있다면
                temp = arr[ni][nj] # 복원 위해 저장해두는 값
                arr[ni][nj] = arr[i][j] - 1 # 무조건 이전 값보다 1 작게
                dfs(ni, nj, route + 1, 0) # 공사 완료
                arr[ni][nj] = temp # 복원

    visited[i][j] = 0

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_h = 0 # 최대 높이 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_h:
                max_h = arr[i][j]

    visited = [[0] * N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_h:
                dfs(i, j, 1, 1)

    print('#{} {}'.format(t, ans))