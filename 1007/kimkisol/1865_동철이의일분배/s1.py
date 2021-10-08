import sys
# 5.34558s
sys.stdin = open('input.txt')


def find_max_probability(idx, temp_p):
    global max_p

    if temp_p <= max_p:
        return
    if idx == N:
        if temp_p > max_p:
            max_p = temp_p
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find_max_probability(idx + 1, temp_p * p[idx][i] / 100)
            visited[i] = 0

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_p = 0

    find_max_probability(0, 1)

    print('#{} {:.6f}'.format(t, max_p * 100))