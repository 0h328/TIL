import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    global cnt
    v[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M:
            if not arr[nr][nc] and not v[nr][nc]:
                dfs(nr, nc)
                v[nr][nc] = 1
                cnt += 1


M, N, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]   # 좌표와 인덱스를 맞추기 위해 NxM 배열로 구성
v = [[0] * M for _ in range(N)]
res = []
cnt = 1     # 값이 0인 좌표를 세어야하므로 1로 놓고 시작

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] += 1          # 좌표에 해당하는 범위를 1로 누적시켜줌

for i in range(N):
    for j in range(M):
        if not arr[i][j] and not v[i][j]:   # 0인 곳과 방문하지 않은 곳만 체크
            dfs(i, j)
            res.append(cnt)
            cnt = 1                 # 분리된 곳 재탐색해야하므로 초기화

print(len(res))
print(*sorted(res))