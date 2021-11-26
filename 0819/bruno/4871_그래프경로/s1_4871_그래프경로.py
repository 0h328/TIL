def dfs(v):
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for w in range(1, V + 1):
                if I[v][w] == 1:    # and not visited[w] 중복이므로 제거
                    stack.append(w)


import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    I = [[0 for _ in range(V+1)] for _ in range(V+1)]   # 인접행렬 초기화
    for i in range(E):
        road = list(map(int, input().split()))
        I[road[0]][road[1]] = 1             # 방향성 그래프
    S, G = map(int, input().split())
    # print(DataFrame(I))

    visited = [0 for _ in range(V+1)]
    dfs(S)

    ans = 0
    if visited[G]:
        ans = 1
    print('#{} {}'.format(tc, ans))