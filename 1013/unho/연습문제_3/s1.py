"""
연습 문제3. DFS 구현 (인접 행렬/인접 리스트/인접 딕셔너리)
"""

def dfs(v):
    stack = [v]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            for e in linked[node]:
                stack.append(e)


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

# dfs 탐색 시작
dfs(1)