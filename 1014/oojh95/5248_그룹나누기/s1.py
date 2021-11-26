import sys
sys.stdin = open('input.txt')


def bfs(n):
    Q.append(n)
    group[n]
    while Q:
        k = Q.pop(0)
        for i in range(1, N+1):
            if visited[k][i] not group[i]:
                Q.append(i)
                group[i]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [[0] * (N+1) for _ in range(N+1)]
    for i in range(0, M*2, 2):
        visited[arr[i]][arr[i+1]] = 1
        visited[arr[i+1]][arr[i]] = 1
    Q = []
    group = [0] * (N+1)
    bfs(1)