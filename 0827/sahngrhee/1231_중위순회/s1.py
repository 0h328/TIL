def in_order(node):
    if node != 0:
        in_order(tree[node][0])
        print('{}'.format(value[node]), end='')
        in_order(tree[node][1])

import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    V = int(input())
    E = V - 1
    tree = [[0 for _ in range(3)] for _ in range(V+1)]
    value = [0]

    for _ in range(V):
        info = list(input().split())
        value.append(info[1])

    for i in range(1, V+1):
        parent_idx = i // 2
        tree[i][2] = parent_idx
        child_left_idx = i * 2
        child_right_idx = (i * 2) + 1
        if child_left_idx <= V:
            tree[i][0] = child_left_idx
        if child_right_idx <= V:
            tree[i][1] = child_right_idx

    print('#{}'.format(test_case), end=' ')
    in_order(1)
    print()