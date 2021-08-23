import sys

sys.stdin = open('input.txt')

T = int(input())

def dfs(start, dest):
    if start == dest:   # 출발지와 목적지가 같아지면 찾은 것이므로 return 1
        return 1
    visited[start] = 1

    for nxt in graph[start]:
        if not visited[nxt]:
            if dfs(nxt, dest):  # dfs 함수 리턴 값이 None이 아니라 1이면 더이상 찾을 필요 없으므로 return 1
                return 1

for tc in range(1, T+1):
    V, E = map(int, input().split())

    visited = [0 for _ in range(V+1)]

    graph = [[] for _ in range(V+1)]    # 인접 리스트

    for _ in range(E):
        start, dest = map(int, input().split())
        graph[start].append(dest)     # 단방향이므로 한쪽에만 append

    S, G = map(int, input().split())

    ans = 1 if dfs(S, G) else 0

    print('#{} {}'.format(tc, ans))