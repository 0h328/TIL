import sys

sys.stdin = open('input.txt')


def DFS(v):
    stack = [v]
    while stack:
        v = stack.pop()
        print(v, end=' ')
        if not visited[v]:
            visited[v] = True
            for w in range(1, V + 1):
                if graph[v][w] == 1 and not visited[w]:
                    stack.append(w)


def DFSS(start):
    stack = [start]
    visited[start] = True
    while stack:
        start = stack.pop()
        print(start, end=' ')
        for i in G[start]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True


def my_DEF(dic_graph, start):
    stack = [start]
    visit = []

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)

            stack.extend(data2[node])

    return visit


# E = 엣지 갯수
V, E = map(int, input().split())

data = list(map(int, input().split()))

graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

for i in range(E):
    graph[data[i * 2]][data[i * 2 + 1]] = 1
    graph[data[i * 2 + 1]][data[i * 2]] = 1

G = [[] for _ in range(V + 1)]

for i in range(1, len(data), 2):
    G[data[i - 1]].append(data[i])
    G[data[i]].append(data[i - 1])

data2 = {}
for i in range(1, len(data), 2):

    if data[i-1] not in data2:
        data2[data[i - 1]] =  []
    if data[i] not in data2:
        data2[data[i]]=[]
    data2[data[i-1]].append(data[i])
    data2[data[i]].append(data[i-1])



# print(graph)
print(G)
#
visited = [False] * (V + 1)
# print(visited)
# DFS(1)
print(data2)
print(my_DEF(data2,1))
DFSS(1)
