import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    N, M, L = map(int, input().split())
    node_list = list(range(N + 1))
    tree = dict()
    for i in node_list:
        tree[i] = 0

    for _ in range(M):
        node, val = map(int, input().split())
        while node > 0:
            tree[node] += val
            node //= 2

    print('#{} {}'.format(case + 1, tree[L]))


