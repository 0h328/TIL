import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    v[r][c] = 1
    # q = deque()
    # q.append((r, c))
    # v[r][c] = 1

    # while q:
    #   (r, c) = q.popleft()

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 1 and not v[nr][nc]:
                v[nr][nc] = 1
                dfs(nr, nc)
                # q.append((nr, nc))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    v = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not v[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)