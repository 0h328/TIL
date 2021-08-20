def dfs(G):
    stack = [0]              # 출발 정점(0) 넣어 놓고 시작
    while stack:             # stack이 빌 동안 반복
        v = stack.pop()      # 특정 정점을 꺼내서
        if not visited[v]:   # 그 정점에 방문하지 않았다면
            visited[v] = 1   # 방문처리하고
            stack += G[v]    # 인접 정점 찾아서 stack에 추가
    return visited[99]       # 최종적으로 정점 99의 방문 여부 반환

import sys
sys.stdin = open('input.txt')
for _ in range(1, 11):
    tc, E = input().split()
    G = [[] for _ in range(100)]
    temp = list(map(int, input().split()))
    visited = [0 for _ in range(100)]
    for idx in range(0, len(temp), 2):
        start = temp[idx]      # 출발 정점
        end = temp[idx+1]      # 도착 정점
        G[start].append(end)   # 인접 리스트 생성
    ans = dfs(G)
    print('#{} {}'.format(tc, ans))