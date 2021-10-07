import sys
sys.stdin = open('input.txt')


def dfs(i, j):
    global path, min_val

    for k in range(2):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:    # and not visited[ni][nj]:
            # visited[ni][nj] = 1
            path += arr[ni][nj]
            dfs(ni, nj)
            # visited[ni][nj] = 0     # 되돌아가기 전에 방문체크 초기화하고
            path -= arr[ni][nj]   # 합에서도 빼줌

    if i == N-1 and j == N-1:   # 마지막 칸에 도달하면
        if path < min_val:        # 기존 최솟값보다 작다면
            min_val = path        # 최솟값 갱신
            return

    if path > min_val:
        return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [1, 0]  # 우, 하
    dj = [0, 1]
    path = arr[0][0]
    min_val = 1690     # 나올 수 있는 합의 최댓값
    # visited = [[0]*N for _ in range(N)]

    dfs(0, 0)

    print('#{} {}'.format(tc, min_val))
