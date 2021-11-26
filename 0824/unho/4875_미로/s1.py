'''
1. 미로의 값이 적혀있는 2차원 배열에서 델타탐색을 이용하여 연결된 경로를 구한다.
2. 도착지에서 출발하여 출발지로 갈수있는지 확인 (DFS)

다시 풀어보기 - 출발점만 찾아놓고, dfs 에서 상하좌우 탐색하며 찾아가기
재귀 활용
'''

import sys
sys.stdin = open('input.txt')



def delta_search():                         # 델타탐색
    global start, end                       # start - 도착부분 / end - 시작부분 (미로의 출구부터 시작하므로)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':           # 2이면 end 에 좌표 저장
                end = (i, j)
            elif maze[i][j] == '3':         # 3이면 start 에 좌표 저장
                start = (i, j)

            if maze[i][j] != 1:             # 현재 좌표가 벽이 아니면
                for k in range(4):
                    y = i + dr[k]
                    x = j + dc[k]

                    if 0 <= x < N and 0 <= y < N and maze[y][x] != '1':     # 상하좌우에 길이 있으면
                        linked[(i, j)] = linked.get((i, j), []) + [(y, x)]  # 현재 좌표와 연결
    print(linked)



def dfs(start):
    stack = [start]

    while stack:                                # 스택이 빌때까지, 더이상 갈 길이 없을때까지
        node = stack.pop()
        if not visited[node[0]][node[1]]:       # 현재위치 방문하지 않았으면
            visited[node[0]][node[1]] = True
            stack.extend(linked[node])          # 다음 갈수있는길 스택에 추가
        if visited[end[0]][end[1]]:             # 출발지점에 도착하면
            return 1                            # 1반환

    return 0                                    # 출구 탈출 못하면 0 반환



test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    maze = [input() for _ in range(N)]

    linked = {}
    visited = [[False]*N for _ in range(N)]

    delta_search()
    answer = dfs(start)

    print('#{} {}'.format(tc, answer))