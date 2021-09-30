from collections import deque
import sys

sys.stdin = open("input.txt")

T = int(input())


def find_start(data):
    starting = []
    height = -1

    for row in range(N):
        for col in range(N):
            if data[row][col] > height:
                height = data[row][col]
                starting = [(row, col)]
            elif data[row][col] == height:
                starting.append((row, col))

    return starting


def bfs(data, start):
    global ans
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] += 1

    while queue:
        cur_row, cur_col = queue.popleft()

        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]

            if 0 <= nxt_row < N and 0 <= nxt_col < N:
                if data[nxt_row][nxt_col] < data[cur_row][cur_col]:
                    queue.append((nxt_row, nxt_col))
                    visited[nxt_row][nxt_col] = visited[cur_row][cur_col] + 1
                    if visited[nxt_row][nxt_col] > ans:
                        ans = visited[nxt_row][nxt_col]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    starting = find_start(data)  # start 지역은 처음 가장 높은 곳으로 고정. 깎고 다시 찾으면 오답.
    for start in starting:
        bfs(data, start)

    for row in range(N):
        for col in range(N):
            for depth in range(1, K + 1):
                data[row][col] -= depth

                for start in starting:
                    bfs(data, start)

                data[row][col] += depth

    print("#{} {}".format(tc, ans))
