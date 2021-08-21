"""
3. dfs - 인접 리스트
"""


def dfs(v):
    visited[v] = 1
    for w in range(V+1):
        if v == temp_2[w][0] and visited[temp_2[w][1]] == 0:
            dfs(temp_2[w][1])



import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))
temp_2 = []
for i in range(0, len(temp), 2):
    temp_2.append(temp[i:i+2])
print(temp_2)

# Graph 초기화

# 방문 표시 초기화
visited = [0] * (V+1)

# dfs 탐색 시작
dfs(1)
print(visited)