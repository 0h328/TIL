import sys
sys.stdin = open('input.txt')

def prim():
    for _ in range(V):
        min_idx = -1
        min_val = 9999999

        for i in range(V+1):
            if not v[i] and key[i] < min_val:
                min_idx = i
                min_val = key[i]
        v[min_idx] = 1

        for i in range(V+1):
            if not v[i] and adj[min_idx][i] < key[i]:
                key[i] = adj[min_idx][i]

    return sum(key)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[9999999 for _ in range(V+1)] for _ in range(V+1)]
    key = [9999999] * (V+1)
    key[0] = 0
    v = [0] * (V+1)

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w

    print('#{} {}'.format(tc, prim()))

