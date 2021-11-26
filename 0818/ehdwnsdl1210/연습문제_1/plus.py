# # stack
# # 그래프 → 현실세계를 추상화
# # 정점(원)들과 간선(사이의 관계선)들의 집합
# # → 컴퓨터에 저장 (그래프 저장, 간선 저장)
# # 1. 인접행렬 (v * v)
#   1 2 3 4 5 (v = 5)
# 1 0 1 1
# 2 1 0 1   1
# 3 1 1 0
# 4       0 1
# 5   1   1 0
#
# 무향인지 유향인지 늘 조심!
#
# # 2. 인접리스트
# 1 → [2, 3]
# 2 → [1, 3, 5]
# 3 → [1, 2]
# 4 → [5]
# 5 → [2, 4]


# 연습문제3
import sys
sys.stdin = open('input2.txt')

V, E = map(int, input().split())  # 정점 갯수  간선 갯수

# 인접 행렬
G = [[0] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
  u, v = map(int, input().split())
  G[u][v] = G[v][u] = 1

for lst in G[1:]:
  print(*lst[1:])

# # 인접 리스트!!
# G = [[] for _ in range(V + 1)]
#
# for _ in range(E):
#   u, v = map(int, input().split())
#   G[u].append(v)
#   G[v].append(u)
#
# for i in range(1, V + 1):
#   print(i, '-->', G[i])


# dfs/재귀
visited = [0] * (V + 1)

def dfs(v):   # 현재 방문하는 정점
  visited[v] = 1
  # print(v, end=' ')
  # 방문하지 않은! 인접정점 찾기
  for w in range(1, V + 1):
    if G[v][w] == 1 and not visited[w]:
      dfs(w)

# dfs(1)