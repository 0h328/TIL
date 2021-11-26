import sys
sys.stdin = open('input.txt')

def dfs(number, success):
    global ans, final
    if success <= ans:
        return

    if number == N:
        if ans < success:
            ans = success
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(number + 1, success * data[number][i])
            visited[i] = 0

T = int(input())

for case in range(T):
    N = int(input())
    data = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 0
    dfs(0, 100)

    print('#{} {:6f}'.format(case + 1, ans))