import sys
sys.stdin = open('input.txt')


def dfs(depth):
    global result, temp
    if depth == N:
        result = min(result, temp)
        return
    if temp > result:
        return

    for col in range(N):
        if not confirm_y[col]:
            temp += arr[depth][col]
            confirm_y[col] = True
            dfs(depth+1)
            temp -= arr[depth][col]
            confirm_y[col] = False
    return


T = int(input())
for test in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    confirm_y = [False] * N
    result, temp = 100, 0

    dfs(0)
    print('#{} {}'.format(test+1, result))
