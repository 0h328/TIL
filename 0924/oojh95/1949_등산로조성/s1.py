import sys
sys.stdin = open('input.txt')

def dfs(r, c, length, dig):
    global result
    if length > result: # 결국은 최대값의 length를 출력해야하니까 각각의 위치에서 저장해주자!
        result = length
    visited[r][c] = 1   # 나 여기 방문했어!
    for i in range(4):  # 사방을 비교하기 위핸 반복문
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if arr[nr][nc] < arr[r][c]:
                dfs(nr, nc, length+1, dig) #dig로 설정하는 것이. 이후에 elif조건에서 스킬이 0이 된 경우를 기억하고 그 값을 계속해서 저장해야함. 만약 1로 설정하면 0이 되었다가 다시 1의 기회가 주어지는 경우가 발생함
            elif dig and arr[nr][nc] - K < arr[r][c]:
                tmp = arr[nr][nc]   # 땅을 파서 깊이를 저장해야 다음 재귀 깊이에서 위의 if조건을 비교할수 있으므로 값을 바꾸어야하는데 이를 초기화 시키기 위해 원본값저장
                arr[nr][nc] = arr[r][c] - 1 # 최대한의 길을 만들기 위해다음 높이는 원래 위치에서 1만 빼준 효율적인 높이를 만들어 줘야함
                dfs(nr, nc, length+1, 0) # 스킬을 사용했으니까 0!
                arr[nr][nc] = tmp # 다시 원래 높이로 돌려주자.
    visited[r][c] = 0 #각 함수의 단계에서 재귀가 모두 끝난 경우 방문기록을 초기화 시켜줘야 다음 기록을 남기는데 활용가능

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_height = 0
    visited = [[0]*N for _ in range(N)]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    for i in range(N):  # 최대높이를 찾아보자
        for j in range(N):
            if arr[i][j] > max_height:
                max_height = arr[i][j]

    result = 0  # 최대값을 여기서 초기화한후 각 지점에서 시행한 최대값은 함수에서 비교해서출력하자
    for i in range(N):  # 최대높이에서 각각의 함수를 시행해보자
        for j in range(N):
            if arr[i][j] == max_height:
                dfs(i, j, 1, 1)
    print('#{} {}'.format(tc, result))