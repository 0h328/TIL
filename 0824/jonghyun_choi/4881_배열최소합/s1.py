import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(i,j):
    global res, check , min_res

    if res > min_res:
        return

    if i == N - 1:
        if res < min_res:
            min_res = res
        return
    else:
        i += 1
        for j in range(N):
            if check[j] == 0:
                res += data[i][j]
                check[j] = 1
                dfs(i, j)
                res -= data[i][j]
                check[j] = 0

for case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    min_res = 987654321
    for j in range(N):
        res = data[0][j]
        check = [0] * N
        check[j] = 1
        dfs(0, j)

    print('#{} {}'.format(case + 1, min_res))