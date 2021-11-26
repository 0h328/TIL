import sys
sys.stdin = open('input.txt')

def dfs(number, cost, s):
    global ans
    if cost > ans:
        return

    if number == N:
        if ans > cost:
            ans = cost
        return

    for i in range(s, N):
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                dfs(number + 1, cost + factory[i][j], i + 1)
                visited[j] = 0


T = int(input())

for case in range(T):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 987654321
    dfs(0, 0, 0)
    print('#{} {}'.format(case + 1, ans))