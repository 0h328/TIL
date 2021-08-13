import sys
sys.stdin = open('input.txt')

M = int(input())

for tc in range(1, M + 1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1. 행 우선
    total_i = 0
    for i in range(N):
        for j in range(N - 1):
            total_i += abs(arr[i][j] - arr[i][j + 1])

    # 2. 열 우선
    total_j = 0
    for j in range(N):
        for i in range(N - 1):
            total_j += abs(arr[i][j] - arr[i + 1][j])

    ans = 2 * (total_i + total_j)

    print('#{} {}'.format(tc, ans))


# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# cnt = 0         #절대값 구할 횟수 카운터
# i, j = 0, -1    #시작 위치
# while cnt < N*N:
#     for k in range(4):
#         n_i, n_j = i+di[k], j+dj[k]
#         if -1<n_i<(N+1) and -1<n_j<N+1
#
#     # arr[i][j]인 경우
#     arr[i-1][j]-arr[i][j]
