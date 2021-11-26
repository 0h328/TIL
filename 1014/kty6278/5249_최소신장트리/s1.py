import sys
sys.stdin = open('input.txt')

def make_set(x):
    tree[x] = x

def find_set(x):
    if tree[x] != x:
        tree[x] = find_set(tree[x])
    return tree[x]

def union(x, y):
    tree[find_set(y)] = find_set(x)


def kruskal():
    global ans
    edge_cnt = idx = 0

    while edge_cnt != v:
        x = edges[idx][0]
        y = edges[idx][1]

        if find_set(x) != find_set(y):
            union(x, y)
            edge_cnt += 1
            ans += edges[idx][2]
        idx += 1


for tc in range(int(input())):
    v, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]  # 간선 정보
    tree = [0] * (v+1)                                              # 상호배타집합에 활용 할 노드 정보 (인덱스를 맞춰주기 위해 V+1)
    edges = sorted(edges, key=lambda x: x[2])                    # 가중치(인덱스 2번)를 기준으로 정렬
    ans = 0

    for i in range(v+1):
        make_set(i)
    kruskal()
    print('#{} {}'.format(tc+1, ans))