import collections
import sys
sys.stdin = open('input.txt')



def bfs(start, end):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    q = collections.deque([start])
    last = q[0]
    cnt = 0

    while q:
        node = q.popleft()
        if node == end:
            return cnt

        if not visited[node[0]][node[1]]:
            visited[node[0]][node[1]] = True

            for k in range(4):
                y = int(node[0]) + dr[k]
                x = int(node[1]) + dc[k]

                if 0 <= x < N and 0 <= y < N and maze[y][x] != '1':
                    q.append((y, x))

        if q and last == node:
            cnt += 1
            last = q[len(q)-1]

    return 0



test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '3':
                start = (i, j)
            if maze[i][j] == '2':
                end = (i, j)

    answer = bfs(start, end)

    print('#{} {}'.format(tc, answer))