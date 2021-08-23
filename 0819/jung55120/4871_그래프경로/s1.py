def dfs(n):
    stack = [n]

    while stack:
        n = stack.pop()

        if not visited[n]:
            visited[n] = 1
            # print('방문 정점: {}, 방문 체크: {}'.format(v, visited))

            for w in range(1, V+1):
                if G[n][w] == 1 and not visited[w]:
                    stack.append(w)

import sys
sys.stdin = open('input.txt')

T = int(input())
# V(ertex), E(dge)
for tc in range(1, T+1):
    V, E = map(int, input().split())

    # Graph 초기화
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]


    # 간선 정보 초기화
    # temp = list(map(int, input().split()))
    # print(temp)

    # 인접 행렬
    for i in range(E):
        start, end = map(int, input().split())
        G[start][end] = 1

    # print(G)

    # 방문 표시 초기화
    visited = [0 for _ in range(V+1)]
    # print(visited)
    # dfs 탐색 시작
    n, m = map(int, input().split())
    dfs(n)
    result = 0
    if visited[m] == 1:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))

    # [[0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 1, 1, 0, 0],
    #  [0, 0, 0, 1, 0, 1, 0],
    #  [0, 1, 1, 0, 0, 0, 0],
    #  [0, 1, 0, 0, 0, 0, 1],
    #  [0, 0, 1, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 1, 0, 0]]
