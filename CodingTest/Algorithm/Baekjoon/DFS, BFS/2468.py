from collections import deque
import sys
sys.stdin = open('input.txt')

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(x, y, h):

    v[x][y] = 1
    q = deque()
    q.append((x, y))

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] > h and not v[nr][nc]:  # h보다 높아야 안전영역, 낮으면 물에 잠김
                    q.append((nr, nc))
                    v[nr][nc] = 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_h = 101 # 주어진 배열의 최저 높이 측정 변수
max_h = 0   # 주어진 배열의 최고 높이 측정 변수

# 2차원 배열에서 min, max값을 한 방에 찾을 수 있는 코드
# min_h = min(map(min, arr))
# max_h = max(map(max, arr))

for i in range(N):
    min_h = min(min(arr[i]), min_h)
    max_h = max(max(arr[i]), max_h)

max_zone = 0
for h in range(min_h, max_h+1):     # 범위는 최저 높이 ~ 최고 높이로 지정
    v = [[0] * N for _ in range(N)] # 매 높이마다 방문리스트 초기화하기 위해 여기에 위치시킴
    cnt = 0                         # 안전영역 체크 돌고올때마다 카운트 초기화
    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and not v[i][j]:  # 물에 잠기지 않는 조건 + 방문하지 않은 경우
                bfs(i, j, h)        # 높이도 매개변수로 추가해주면 시간 감소?
                cnt += 1

    if max_zone < cnt:  # 최대 안전영역 개수 갱신
        max_zone = cnt

print(max_zone)