# 인접 리스트 - 재귀

def dfs(v):

    visited[v] = 1                                          # 방문 체크
    #print('방문 정점: {}, 방문 체크: {}'.format(v, visited))
    for w in G[v]:                                          # 정점 v의 인접 정점 w 중에서
        if not visited[w]:                                  # 아직 방문하지 않은 곳이 있다면
            dfs(w)                                          # 호출!

import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    ans = 0
    T, V = map(int, input().split())
    temp = list(map(int, input().split()))
    G = [[] for _ in range(100)]
    visited = [0 for _ in range(100)]
    for i in range(1, len(temp), 2):
        G[temp[i-1]].append(temp[i])
    dfs(0)
    if visited[99] == 1:
        ans = 1

    print('#{} {}'.format(test_case, ans))