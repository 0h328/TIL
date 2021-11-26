from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(row, col):
    global result
    drow = [0, 1, -1, 0]
    dcol = [-1, 0, 0, 1]
    que = deque()
    que.append((row, col))
    visited[row][col] = 1 # 시작지점 방문 했다고 표현

    while que:
        row, col = que.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0 <= nrow < 16 and 0 <= ncol < 16 and visited[nrow][ncol] == 0:  # 방문하지 않은 경우만 판단
                if maze[nrow][ncol] == 3:  # 3이 존재하는 경우 방문값 출력
                    result = 1
                    return result
                if maze[nrow][ncol] == 0:  # 갈수 있는 길인 경우 방문 체크
                    visited[nrow][ncol] = 1
                    que.append((nrow, ncol))  # 'que'에 갈 수 있는 루트 저장
    return result


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    result = 0
    visited = [[0] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[j][i] == 2:
                bfs(j, i)
                print('#{} {}'.format(tc, result))
    # 3 위치 찾을까? 했는데 필요 없음