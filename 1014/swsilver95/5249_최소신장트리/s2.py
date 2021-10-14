import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


# 2. kruskal을 이용한 풀이
def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x


def kruskal(edges):
    global answer
    for edge in edges:
        weight, n1, n2 = edge
        if find(n1) != find(n2):
            union(n1, n2)
            answer += weight


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    parent = [i for i in range(V + 1)]
    edges = []

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))

    edges.sort()
    answer = 0
    kruskal(edges)

    print('#{} {}'.format(tc, answer))
