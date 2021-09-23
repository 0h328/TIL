# 노드의 합

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = list(map(int, input().split())) # N: 노드의 수, M: 리프노드의 수, L: 출력할 노드번호

    tree = [0] * (N+1)


    for i in range(M):
        leaf_node, num = map(int, input().split())
        tree[leaf_node] = num

    for i in range(N//2, 0, -1):
        try:
            tree[i] = tree[i*2] + tree[i*2+1]
        except:
            tree[i] = tree[i*2]

    print('#{} {}'.format(tc, tree[L]))






