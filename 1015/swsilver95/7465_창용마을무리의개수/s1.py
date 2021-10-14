import sys
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


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())    # N: 사람 번호 / M: 간선 수
    parent = [0] * (N + 1)

    for i in range(N + 1):
        parent[i] = i

    for _ in range(M):
        n1, n2 = map(int, input().split())
        union(n1, n2)

    answer = set()
    for j in range(1, N + 1):
        answer.add(find(parent[j]))

    print('#{} {}'.format(tc, len(answer)))