import sys
from collections import deque
sys.stdin = open('input.txt')


# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs():
    global q, visited

    while q:
        i, j = q.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            # 범위 안, 값이 L이고 방문 안했으면 +1
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 'L' and visited[ni][nj] == -1:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)] # input 리스트로 받아오면 느려짐
    visited = [[-1] * M for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W': # 물을 미리 담아두기
                q.append((i, j))
                visited[i][j] = 0

    bfs()

    ans = 0
    for row in visited:
        for val in row:
            ans += val

    print('#{} {}'.format(t, ans))