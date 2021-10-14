import sys
sys.stdin = open('input.txt')

def dfs(start):
    for i in range(1, N + 1):
        if peer[start][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)


T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    peer = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for i in range(len(data)//2):
        peer[data[i * 2]][data[i * 2 + 1]] = 1
        peer[data[i * 2 + 1]][data[i * 2]] = 1

    cnt = 0
    for i in range(1, N + 1):
        if visited[i] == 0:
            cnt += 1
            dfs(i)
    print('#{} {}'.format(case + 1, cnt))