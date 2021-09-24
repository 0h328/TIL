def post_order(node):
    global plus
    if node != 0:
        post_order(tree[node][0])
        post_order(tree[node][1])
        plus += value[node]

import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [[0 for _ in range(3)] for _ in range(N+1)]
    value = [0] * (N+1)
    plus = 0

    for _ in range(M):
        leaf, val = map(int, input().split())
        value[leaf] = val

    for i in range(1, N+1):
        parent_idx = i // 2
        tree[i][2] = parent_idx
        child_left_idx = i * 2
        child_right_idx = (i * 2) + 1
        if child_left_idx <= N:
            tree[i][0] = child_left_idx
        if child_right_idx <= N:
            tree[i][1] = child_right_idx

    post_order(L)
    print('#{} {}'.format(test_case, plus))