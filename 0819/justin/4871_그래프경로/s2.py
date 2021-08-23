def dfs(start, goal):
    stack = [start]
    while stack:
        v = stack.pop()
        if not visited[v]:      # 그곳에 아직 방문하지 않았다면
            visited[v] = 1      # 방문 처리
            stack += G[v]   # 인접 정점 추가
    return visited[goal]

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        G[s].append(e)
    """
    인접 리스트로 그래프를 구현
    [
        0: [] => idx 편의상 생성
        1: [4, 3]
        2: [3, 5]
        3: []
        4: [6]
        5: []
        6: []
    ]
    """
    start, goal = map(int, input().split())
    ans = dfs(start, goal)
    print('#{} {}'.format(tc, ans))