import sys
from pprint import pprint
from collections import deque

sys.stdin = open('input.txt')


def bfs(node):
    global answer

    q = deque([node])
    visited[node[0]][node[1]] = 1

    while q:
        node = q.popleft()
        answer += 1
        for k in START[tunnel[node[0]][node[1]]]:
            y = node[0] + dr[k]
            x = node[1] + dc[k]

            if 0 <= y < N and 0 <= x < M and not visited[y][x] and tunnel[y][x] in DIRECTION[k]:
                visited[y][x] = visited[node[0]][node[1]] + 1
                if visited[y][x] == L + 1:
                    answer += len(q)
                    return
                q.append((y, x))


START = {
    1: [0, 1, 2, 3],
    2: [0, 2],
    3: [1, 3],
    4: [0, 1],
    5: [1, 2],
    6: [2, 3],
    7: [0, 3],
}

DIRECTION = {
    0: [1, 2, 5, 6],
    1: [1, 3, 6, 7],
    2: [1, 2, 4, 7],
    3: [1, 3, 4, 5],
}

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    answer = 0

    bfs((R, C))

    print('#{} {}'.format(tc, answer))