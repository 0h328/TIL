import sys
sys.stdin = open('input.txt')

def dfs(row, cost):
    global ans
    if cost > ans:
        return

    if len(row) == N:
        if ans > cost:
            ans = cost
        return

    for i in range(N):
        if i not in row:
            row.append(i)
            for j in range(N):
                if visited[j] == 0:
                    visited[j] = 1
                    dfs(row, cost + factory[i][j])
                    visited[j] = 0
            row.pop()


T = int(input())

for case in range(T):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 987654321
    dfs([], 0)
    print('#{} {}'.format(case + 1, ans))