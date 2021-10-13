"""
연습 문제4. BFS 구현 (인접 행렬/인접 리스트/인접 딕셔너리)
"""


def bfs(v):
    queue = [v]

    while queue:
        node = queue.pop(0)
        if not visited[node]:
            visited[node] = 1
            for e in linked[node]:
                queue.append(e)


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
li = list(map(int, input().split()))

# Graph 초기화
linked = {i:[] for i in range(1, V+1)}

for idx in range(len(li)//2):
    linked[li[idx*2]].append(li[idx*2+1])
    linked[li[idx*2+1]].append(li[idx*2])

# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
bfs(1)