"""
4. bfs - 1번 노드에서 가장 멀리 떨어진 노드 찾기 (거리에 대한 정보 담아 놓기)
"""

def bfs(v):
    queue = [v]
    visited[v] = 1
    max_val = 0

    while queue:
        cur = queue.pop(0)
        for w in G[cur]:
            if not visited[w]:
                queue.append(w)
                visited[w] = visited[cur] + 1
                if visited[w] > max_val:
                    max_val = visited[w]
    print(max_val)


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())
# 간선 정보 초기화
temp = list(map(int, input().split()))
# Graph 초기화
G = [[] for _ in range(V+1)]
for i in range(E):
    G[temp[2*i]].append(temp[2*i+1])
    G[temp[2*i+1]].append(temp[2*i])
# 방문 표시 초기화
visited = [0 for _ in range(V+1)]
# bfs 탐색 시작
bfs(1)