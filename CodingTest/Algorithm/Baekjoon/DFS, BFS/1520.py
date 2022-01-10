import sys
sys.stdin = open('input.txt')

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def dfs(r, c):
    if r == M-1 and c == N-1:   # 오른쪽 최하단 좌표인 경우
        return 1                # 하나의 경로

    if dp[r][c] == -1:          # -1인 경우에만 방문하지 않았으므로
        dp[r][c] = 0            # 0으로 바꾸고

        for i in range(4):      # 탐색 실행
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < M and 0 <= nc < N:
                if arr[r][c] > arr[nr][nc]: # 현재 위치가 다음 위치보다 커야함
                    dp[r][c] += dfs(nr, nc) # 마지막 좌표에 도착했을때 1이 리턴되면서 지나온 거리를 +1로 누적시켜줌

    return dp[r][c]

M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
# 0으로 하면 방문한 곳이 모두 1로 되면서 누적해서 더해질때 계속 +1됨
# 그래서 -1로 해야 방문한 곳이 모두 0으로 되고, 누적해서 더해질때 1로만 유지됨

print(dfs(0, 0))