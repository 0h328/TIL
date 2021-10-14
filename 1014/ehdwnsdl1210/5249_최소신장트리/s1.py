import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

def prim():
    for _ in range(V):
        min_idx = -1
        min_value = 987654321

        for i in range(V + 1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]
        visited[min_idx] = 1

        for i in range(V + 1):
            if not visited[i] and grp[min_idx][i] < key[i]:
                key[i] = grp[min_idx][i]
    return sum(key)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    grp = [[987654321] * (V+1) for _ in range(V+1)]
    key = [987654321] * (V + 1)
    key[0] = 0
    visited = [0] * (V + 1)

    for i in range(E):
        n1, n2, w = map(int, input().split())
        grp[n1][n2] = w
        grp[n2][n1] = w

    # print(DataFrame(adj))

    print('#{} {}'.format(tc, prim()))

#1 2
#2 13
#3 22