import sys
from heapq import *
sys.stdin = open('input.txt', 'r')


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


def price(A, B):
    a1, b1 = A
    a2, b2 = B
    d = (a1 - a2)**2 + (b1 - b2)**2
    return d * E


def kruskal(edges):
    global answer
    for edge in edges:
        weight, n1, n2 = edge
        if find(n1) != find(n2):
            union(n1, n2)
            answer += weight


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    INF = 1e9
    parent = [0] * N
    answer = 0
    for i in range(N):
        parent[i] = i

    edges = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            node1 = (X[i], Y[i])
            node2 = (X[j], Y[j])
            tmp = price(node1, node2)
            edges.append((tmp, i, j))
    edges.sort()

    kruskal(edges)
    print('#{} {}'.format(tc, round(answer)))