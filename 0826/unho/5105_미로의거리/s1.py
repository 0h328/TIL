import collections
import sys
sys.stdin = open('input.txt')



def bfs(start):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    q = collections.deque()
    q.append(start)

    while q:
        node = q.popleft()
        visited[node[0]][node[1]] += 1
        for k in range(4):
            y = node[0] + dr[k]
            x = node[1] + dc[k]

            if 0 <= x < N and 0 <= y < N and maze[y][x] != '1' and not visited[y][x]:
                q.append((y, x))
                visited[y][x] = visited[node[0]][node[1]]

                if maze[y][x] == '3':
                    return 1

    return 0



test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start = (i, j)
            elif maze[i][j] == '3':
                end = (i, j)

    coordinate = bfs(start)


    if coordinate == 0:
        answer = 0
    else:
        answer = visited[end[0]][end[1]] - 1

    print('#{} {}'.format(tc, answer))