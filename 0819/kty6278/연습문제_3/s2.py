# 인접 행렬 - 재귀
# 재귀는 반드시 디버거 켜놓고 확인해주세요!

def dfs(v):
    if not visited[v]:                                          # 방문하지 않았다면 방문 체크
        visited[v] = 1
    print('방문 정점: {}, 방문 체크 확인: {}'.format(v, visited))
    for w in range(1, V+1):                                     # 모든 정점을 돌며
        if G[v][w] == 1 and not visited[w]:                     # 해당 정점(w)이 정점 v의 인접 정점이고 아직 방문하지 않았다면
            dfs(w)                                              # 방문 처리를 위한 재귀 호출 -> 언제 함수가 종료되는지 고민해보세요!

import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

# 정점 정보를 활용하여 그래프 초기화하는 방법
for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1

dfs(1)