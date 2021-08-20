import sys
sys.stdin = open('input2.txt')

T = int(input())

def count_grid(data, N, K):
    i = 0
    res = 0
    while i < N:
        cnt = 0
        j = 0
        while j <= N:
            if j == N:
                if cnt == K:
                    res += 1
                break
            if cnt == K and j < N - 1 and data[i][j + 1] == 0:
                res += 1
                break
            if data[i][j] == 1:
                cnt += 1
            elif data[i][j] == 0:
                cnt = 0
            j += 1

        i += 1
    return res

for case in range(T):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    zip_grid = list(zip(*grid))
    cnt = 0
    cnt += count_grid(grid, N, K)
    cnt += count_grid(zip_grid, N, K)
    print('#{} {}'.format(case + 1, cnt))