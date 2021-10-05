import sys
sys.stdin = open('input.txt')

# 각 칸에서는 오른쪽 또는 아래로만 이동 가능

def find_route(r, c, result):
    global min_sum

    if min_sum < result:
        return

    if r == N-1 and c == N-1:
        result += arr[r][c]
        if min_sum > result:
            min_sum = result
            return

    else:
        for k in range(2):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= r < N and 0 <= c < N and not visited[r][c]:
                visited[r][c] = 1
                find_route(nr, nc, result + arr[r][c])
                visited[r][c] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0
    min_sum = N * N * 9
    dr = [0, 1]
    dc = [1, 0]

    find_route(0, 0, 0)

    print('#{} {}'.format(tc, min_sum))