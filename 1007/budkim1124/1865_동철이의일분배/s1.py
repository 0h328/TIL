import sys
sys.stdin = open("input.txt")


def dfs(i, tmp):
    global result

    if result >= tmp:   # 가지치기
        return

    if i == N:
        result = tmp
        return

    for k in range(N):
        if not visited[k]:
            visited[k] += 1
            # tmp = tmp * (arr[k][i] / 100)
            dfs(i+1, tmp * (arr[k][i] /100))
            visited[k] -= 1
            # tmp = tmp / (arr[k][i] / 100)


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    result = 0
    # tmp = 0
    dfs(0, 1)

    print("#{} {}".format(t+1, result*100))
