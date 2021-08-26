from collections import deque
import sys
sys.stdin = open('input.txt')

T = 10

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1

    while queue:
        cur_row, cur_col = queue.popleft()

        for i in range(4):      # 상하좌우 4방향 탐색
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]
            if 0 <= nxt_row < N and 0 <= nxt_col < N and data[nxt_row][nxt_col] != '1' and not visited[nxt_row][nxt_col]:
                if data[nxt_row][nxt_col] == '3':   # 도착지인 '3' 지점 찾으면
                    return 1                        # 1 return 하며 함수 종료
                queue.append([nxt_row, nxt_col])
                visited[nxt_row][nxt_col] = 1
    # while 문을 다 돈 경우, 목적지에 다를 수 없으므로 return 0
    return 0


for _ in range(T):
    tc = int(input())
    N = 16
    data = [list(input()) for _ in range(N)]    # 2차원 맵 입력

    for row in range(N):
        for col in range(N):
            if data[row][col] == '2':   # 시작 지점 찾기
                start = [row, col]
                break

    visited = [[0] * N for _ in range(N)]
    print('#{} {}'.format(tc, bfs(start)))