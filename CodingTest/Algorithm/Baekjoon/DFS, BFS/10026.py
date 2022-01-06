from collections import deque
import sys
sys.stdin = open('input.txt')

dr = [1, 0, -1, 0]
dc = [0 ,1, 0, -1]

def R(x, y):

    q = deque()
    q.append((x, y))
    v[x][y] = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if not v[nr][nc] and arr[nr][nc] == 'R':
                    q.append((nr, nc))
                    v[nr][nc] = 1


def G(x, y):

    q = deque()
    q.append((x, y))
    v[x][y] = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if not v[nr][nc] and arr[nr][nc] == 'G':
                    q.append((nr, nc))
                    v[nr][nc] = 1


def B(x, y):

    q = deque()
    q.append((x, y))
    v[x][y] = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if not v[nr][nc] and arr[nr][nc] == 'B':
                    q.append((nr, nc))
                    v[nr][nc] = 1


N = int(input())

# 적록색약이 아닐때
arr = [list(input()) for _ in range(N)]
v = [[0] * N for _ in range(N)]
not_cl_bl = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R' and not v[i][j]:    # 방문 체크안하면 방문한 곳 다시감
            R(i, j)         # 인접한 R영역 다돌고
            not_cl_bl += 1  # R색상 +1
        elif arr[i][j] == 'G' and not v[i][j]:  # 방문 체크안하면 방문한 곳 다시감
            G(i, j)         # 인접한 G영역 다돌고
            not_cl_bl += 1  # G색상 +1
        elif arr[i][j] == 'B' and not v[i][j]:  # 방문 체크안하면 방문한 곳 다시감
            B(i, j)         # 인접한 B영역 다돌고
            not_cl_bl += 1  # B색상 +1

# 적록색약일때
v = [[0] * N for _ in range(N)] # 방문리스트 초기화
cl_bl = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':    # R이랑 G랑 같이 구분되므로
            arr[i][j] = 'G'     # R을 G로 바꿔버린다.

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G' and not v[i][j]:    # 방문 체크안하면 방문한 곳 다시감
            G(i, j)     # R을 G로 바꿨으니 인접한 모든 G영역 다돌고
            cl_bl += 1  # G색상 +1
        elif arr[i][j] == 'B' and not v[i][j]:  # 방문 체크안하면 방문한 곳 다시감
            B(i, j)     # 인접한 B영역 다돌고
            cl_bl += 1  # B색상 +1

print(not_cl_bl, cl_bl)