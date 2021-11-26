from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1

    while queue:
        cur_row, cur_col = queue.popleft()
        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]
            if 0 <= nxt_row < N and 0 <= nxt_col < N and data[nxt_row][nxt_col] != '1' and not visited[nxt_row][nxt_col]:
                if data[nxt_row][nxt_col] == '3':
                    return visited[cur_row][cur_col] - 1    # 도착지까지 거리는 시작점을 1로 두었을 때 시작과 끝을 뺀 값이므로 cur 좌표까지의 합계에서 1 빼줌
                visited[nxt_row][nxt_col] = visited[cur_row][cur_col] + 1   # visited를 이전 좌표 값 거리에서 1씩 더해줌. 나머지는 미로 1과 동일
                queue.append([nxt_row, nxt_col])
    return 0


for tc in range(1, T+1):
    N = int(input())
    data = [list(input()) for _ in range(N)]

    for row in range(N):
        for col in range(N):
            if data[row][col] == '2':
                start = [row, col]
                break

    visited = [[0] * N for _ in range(N)]

    print('#{} {}'.format(tc, bfs(start)))