import sys
sys.stdin = open('input.txt')


def dfs(idx, total):
    global res

    if total >= res:
        return

    if all(visited):                    # 모든 지점 다 방문했으면
        total += arr[idx][0]            # 0으로 이동한 후에 갱신
        if total < res:
            res = total

    for i in range(1, N):
        if not visited[i]:
            visited[i] = 1
            dfs(i, total + arr[idx][i])
            visited[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [1] + [0 for _ in range(N-1)]
    print(visited)
    res = 10000
    # 1-(2~N-1)-1 어디를 먼저 가냐? 이 순서를 정하면 더할 값은 정해짐
    dfs(0, 0)
    print('#{} {}'.format(t, res))