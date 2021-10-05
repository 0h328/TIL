import sys

sys.stdin = open('input.txt')

T = int(input())


def dfs(x, cnt):
    global ans, temp_ans
    if cnt == N - 1:
        temp_ans += num_list[x][0]
        if ans > temp_ans:
            ans = temp_ans
        temp_ans -= num_list[x][0]

    for k in range(1, N):
        if visited[k] == 0:
            temp_ans += num_list[x][k]
            visited[k] = 1
            dfs(k, cnt + 1)
            temp_ans -= num_list[x][k]
            visited[k] = 0


for tc in range(1, T + 1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    ans = 50000
    for i in range(1, N):
        visited = [0] * N
        visited[i] = 1
        temp_ans = num_list[0][i]
        dfs(i, 1)
    print('#{} {}'.format(tc,ans))
