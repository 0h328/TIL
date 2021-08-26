"""
3. bfs - 인접 딕셔너리 구현
"""
from collections import deque
def bfs(v):
    q=[]
    visit = []
    q.append(v)

    while q:
        node = q.pop(0)
        if node not in visit:
            visit.append(node)
            q.extend(graph[node])

    return visit


import sys
sys.stdin = open('input.txt')
a,b = list(map(int,input().split()))

data = list(map(int,input().split()))
graph = {x: [] for x in range(max(data) + 1)}
for i in range(0,len(data),2):
    graph[data[i]].append(data[i+1])
print(graph)
# V(ertex), E(dge)

# 간선 정보 초기화

# Graph 초기화

# 방문 표시 초기화

# bfs 탐색 시작
print(bfs(1))