"""
3. bfs - 인접 딕셔너리 구현
"""

def bfs(v):
    visited[v] = 1
    queue = [v]

    while queue:
        p = queue.pop(0)

        for j in range(V + 1):
            if (j in G.get(p, [])) and not visited[j]:
                queue.append(j)
                visited[j] = visited[p] + 1


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
tmp = list(map(int, input().split()))

# Graph 초기화
G = dict()
for i in range(E):
    s, e = tmp[i*2], tmp[i*2 + 1]
    if not G.get(s, 0):
        G[s] = []
        G[s].append(e)
    else:
        G[s].append(e)
# print(G)

# 방문 표시 초기화
visited = [0] * (V + 1)

# bfs 탐색 시작
bfs(1)
print(visited)