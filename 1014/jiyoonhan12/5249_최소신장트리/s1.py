import sys
sys.stdin = open('input.txt')

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

def kruskal():
    global ans
    edge_cnt = idx = 0

    while edge_cnt != V:
        x = edges[idx][0]
        y = edges[idx][1]

        if find_set(x) != find_set(y):
            union(x, y)
            edge_cnt += 1
            ans += edges[idx][2]
        idx += 1


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x:x[2])
    p = [0] * (V+1)
    ans = 0
    for i in range(V+1):
        make_set(i)
    kruskal()
    print('#{} {}'.format(t, ans))