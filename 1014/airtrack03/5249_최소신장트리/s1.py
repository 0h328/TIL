import sys

sys.stdin = open('input.txt')

def make_set(n):
    p[n] = n

def find_set(n):
    while n != p[n]:
        n = p[n]
    return n

def union(v1, v2):
    p[find_set(v2)] = find_set(v1)

def kruskal():
    global ans
    cnt, edge_idx = 0, 0

    while cnt != V:
        v1 = edges[edge_idx][0]
        v2 = edges[edge_idx][1]

        if find_set(v1) != find_set(v2):
            union(v1, v2)
            cnt += 1
            ans += edges[edge_idx][2]

        edge_idx += 1


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    p = [0] * (V+1)
    for i in range(V+1):
        make_set(i)

    edges = []
    for _ in range(E):
        v1, v2, w = map(int, input().split())
        edges.append((v1, v2, w))

    ans = 0
    edges.sort(key=lambda x: x[2])

    kruskal()

    print('#{} {}'.format(tc, ans))