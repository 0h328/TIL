import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(start):
    global answer

    q = deque(start)

    while q:
        node = q.popleft()
        answer += visited[node[0]][node[1]]

        for k in range(4):
            y = node[0] + dr[k]
            x = node[1] + dc[k]

            if 0 <= y < N and 0 <= x < M and not visited[y][x]:
                visited[y][x] = visited[node[0]][node[1]] + 1
                q.append((y, x))


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    beach = [input() for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    start = []
    answer = 0

    for i in range(N):
        for j in range(M):
            if beach[i][j] == 'W':
                visited[i][j] = -1
                for k in range(4):
                    y = i + dr[k]
                    x = j + dc[k]

                    if 0 <= y < N and 0 <= x < M and beach[y][x] == 'L' and not visited[y][x]:
                        visited[y][x] = 1
                        start.append((y, x))

    bfs(start)

    print('#{} {}'.format(tc, answer))