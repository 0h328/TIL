import sys
from pandas import DataFrame

sys.stdin = open('input.txt')

for test in range(1,1+int(input())):
    N = int(input())
    data = []
    visited = [[-1]*N for _ in range(N)]
    core = []
    for i in range(N):
        temp = list(map(int,input().split()))
        data.append(temp)
        for j in range(N):
            if temp[j]:
                core.append((i,j))
                visited[i][j]=0 # core position
    # print(core)
    linked_core = 0
    linked_line = 0
    distance_line = [[] for _ in range(len(core))]
    # 1 모든 core에서 최소 거리 확인
    for i in range(len(core)):
        tmp = []
        tmp.append(core[i][0]) # 상
        tmp.append((N - core[i][0]) - 1)  # 하
        tmp.append(core[i][1])  # 좌
        tmp.append((N - core[i][1]) - 1)  # 우
        distance_line[i] = tmp

    def backtrack(visit, index=0, total_line=0, total_core=0):
        if index == len(core):
            global linked_line, linked_core
            if linked_core < total_core:
                linked_core = total_core
                linked_line = total_line
                # print(total_core, total_line)
                # print(*visit, sep='\n', end='\n\n')

            elif linked_core == total_core:
                if linked_line > total_line:
                    linked_line = total_line
                    # print(total_core, total_line)
                    # print(*visit, sep='\n', end='\n\n')

        else:# 방향 0,1,2,3, : 상하좌우
            cnt = 0
            if core[index][0] == 0 or core[index][0] == len(data) - 1 or core[index][1] == 0 or core[index][1] == len(data) - 1:
                backtrack(visit, index + 1, total_line, total_core + 1)
            else:
                for i in range(4):
                    if find_cross(core[index][0], core[index][1], i, visit):
                        cnt += 1
                        continue
                    tmp_visit = [vs[:] for vs in visit]
                    paint(core[index][0], core[index][1], i, tmp_visit)
                    backtrack(tmp_visit, index + 1, total_line + distance_line[index][i], total_core + 1)

                if cnt == 4:
                    backtrack(visit, index + 1, total_line, total_core)


    def find_cross(x, y, direction, visit):
        # cross 하는지만 확인
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dx = x + delta[direction][0]
        dy = y + delta[direction][1]
        while 0 <= dx < len(visit) and 0 <= dy < len(visit):
            if visit[dx][dy] > -1:
                return True
            dx += delta[direction][0]
            dy += delta[direction][1]
        return False

    def paint(x, y, direction, visit):
        # 해당 방향으로 그림
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dx = x + delta[direction][0]
        dy = y + delta[direction][1]
        while 0 <= dx < len(visit) and 0 <= dy < len(visit):
            visit[dx][dy] = 1
            dx += delta[direction][0]
            dy += delta[direction][1]


    backtrack(visited)
    print("#{} {}".format(test, linked_line))

# def DFS(x, y):
#     ans = []
#     for i in range(4):
#         temp = 1e9
#         cnt = 0
#         nx = x + dx[i]
#         ny = y + dy[i]
#         while 0 <= nx < N and 0 <= ny < N:
#             if data[nx][ny] == 1:
#                 cnt = temp+1
#                 break
#             nx += dx[i]
#             ny += dy[i]
#             cnt += 1
#
#         if cnt <temp:
#             temp = cnt
#         ans.append(temp)
#     return min(ans)
#
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# for test in range(1, 1 + int(input())):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     start = []
#     for i in range(1, N - 1):
#         for j in range(1, N - 1):
#             if data[i][j] == 1:
#                 start.append((i, j))
#     # print(start)
#     answer = 0
#     for i in start:
#         x, y = i
#         # answer += DFS(x, y)
#         print(DFS(x, y))
