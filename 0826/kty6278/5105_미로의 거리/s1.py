from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(row, col):
    global result
    drow = [0, 1, -1, 0]
    dcol = [-1, 0, 0, 1]
    que = deque()
    que.append((row, col))
    while que:
        row, col = que.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0 <= nrow < N and 0 <= ncol < N and visited[nrow][ncol] == 0:  # 방문하지 않은 경우만 판단
                if maze[nrow][ncol] == 3:  # 3이 존재하는 경우 방문값 출력
                    result = visited[row][col]
                    return result
                if maze[nrow][ncol] == 0:  # 0인 경우 누적 방문값 만든다.
                    visited[nrow][ncol] = visited[row][col] + 1
                    que.append((nrow, ncol))  # 'que'에 갈 수 있는 루트 저장
    return result

for tc in range(int(input())):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    result = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[j][i] == 2:
                bfs(j, i)
                print('#{} {}'.format(tc+1, result))