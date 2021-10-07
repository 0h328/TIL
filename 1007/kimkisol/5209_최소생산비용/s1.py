import sys

sys.stdin = open('input.txt')


def find_min_cost(idx, temp_cost):
    global min_cost

    if temp_cost >= min_cost:
        return
    if idx == N:
        if temp_cost < min_cost:
            min_cost = temp_cost
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find_min_cost(idx + 1, temp_cost + costs[idx][i])
            visited[i] = 0

T = int(input())

for t in range(1, T + 1):
    N = int(input())  # N: 제품수 = 행열크기
    costs = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_cost = 99 * N

    find_min_cost(0, 0)

    print('#{} {}'.format(t, min_cost))