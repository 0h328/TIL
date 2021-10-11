import sys
sys.stdin = open("input.txt")


def dfs(i, total):
    global result

    if result < total:
        return

    if i == N:
        result = min(result, total)
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(i + 1, total + arr[i][j])   # 합에 리스트 값을 더해주면서 dfs
            visited[j] = 0

T = int(input())

for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 1500
    visited = [0] * N

    dfs(0,0)

    print("#{} {}".format(t+1, result))