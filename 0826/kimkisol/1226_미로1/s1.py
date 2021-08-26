import sys

sys.stdin = open('input.txt')

#dfs 적용...
def Maze(map_list):
    # 시작점 좌표 찾기
    for i in range(16):
        for j in range(16):
            if map_list[i][j] == 2:
                row, col = i, j
                break

    # 탐색하기
    visited = [[0] * 16 for _ in range(16)]  # 좌표 방문여부
    dr = [-1, 1, 0, 0]  # 상하좌우 행
    dc = [0, 0, -1, 1]  # 열
    stack = [(row, col)]  # 갔던 길
    visited[row][col] = 1

    while stack:
        now = stack[-1] # 현재위치 = 마지막 스택 값
        for i in range(4):
            row, col = now[0] + dr[i], now[1] + dc[i]
            if map_list[row][col] == 3:
                return 1
            if map_list[row][col] == 0 and visited[row][col] == 0:
                stack.append((row, col))
                visited[row][col] = 1
                break
        else:
            stack.pop() # 현재 위치 꺼내기(갔던길에서 뒤로 돌아가기)

    return 0

for _ in range(1, 11):
    N = int(input())
    map_list = [list(map(int, list(input()))) for _ in range(16)]
    print('#{} {}'.format(N, Maze(map_list)))