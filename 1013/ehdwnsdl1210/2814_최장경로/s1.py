'''
DFS
시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면,
가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서
다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
'''

import sys
sys.stdin = open('input.txt')

def DFS(n, cnt):
    global max_cnt

    if max_cnt < cnt:
        max_cnt = cnt

    for i in range(1, N+1):
        if visited[i] == 0 and adj[n][i] == 1:
            visited[i] = 1
            DFS(i, cnt+1)
            visited[i] = 0      # 다른 곳 탐색할 땐 원복 필수 (백트래킹)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    # print(adj)

    for _ in range(M):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1
    # print(adj)

    max_cnt = 0

    for i in range(1, N+1):         # 어디가 시작인지 모름 (1이 시작이 아님)
        visited = [0] * (N + 1)     # 이게 밖이면
        visited[i] = 1              # 처음 방문 하고 감
        DFS(i, 1)                   # 좌표랑 cnt
        # visited[i] = 0            # visited를 밖에 만들면 백트래킹 필요

    print('#{} {}'.format(tc, max_cnt))
#1 1
#2 3