# 1. sol

import sys

sys.stdin = open('input.txt')


def Maze(map_list):
    # 시작점 좌표 찾기
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if map_list[i][j] == 2:
                row, col = i, j
                break

    # 탐색하기
    visited = [[0] * (N + 2) for _ in range(N + 2)]  # 좌표 방문여부
    dr = [-1, 1, 0, 0]  # 상하좌우 행
    dc = [0, 0, -1, 1]  # 열
    stack = [(row, col)]  # 갔던 길
    visited[row][col] = 1

    while stack:
        now = stack[-1]  # 현재위치 = 마지막 스택 값
        for i in range(4):
            row, col = now[0] + dr[i], now[1] + dc[i]  # 새로 움직였다고 가정했을 때 좌표(row, col)
            if map_list[row][col] == 3:
                return visited[now[0]][now[1]] - 1
            if map_list[row][col] == 0 and visited[row][col] == 0:
                stack.append((row, col))
                visited[row][col] = visited[now[0]][now[1]] + 1
                break
        else:
            stack.pop()  # 현재 위치 꺼내기(갔던길에서 뒤로 돌아가기)

    return 0


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    map_list = [[1] * (N + 2)] + [[1] + list(map(int, input())) + [1] for _ in range(N)] + [[1] * (N + 2)]
    print('#{} {}'.format(t, Maze(map_list)))
