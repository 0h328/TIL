import sys

sys.stdin = open('input.txt')


def dfs(x, total):
    global answer

    if x == N:
        if answer > total:
            answer = total
        return

    if answer < total:  # 가지치기
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(x + 1, total + data[x][i])
            visited[i] = 0


for test in range(1, 1 + int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    answer = 1e9

    dfs(0, 0)

    print('#{} {}'.format(test, answer))
