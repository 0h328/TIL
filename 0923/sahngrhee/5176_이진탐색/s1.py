def in_order(node):
    global num
    if node != 0:
        in_order(tree[node][0])
        num.append(node)
        in_order(tree[node][1])


import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    tree = [[0 for _ in range(3)] for _ in range(N+1)]
    num = []

    for i in range(1, N+1):
        parent_idx = i // 2
        tree[i][2] = parent_idx
        child_left_idx = i * 2
        child_right_idx = (i * 2) + 1
        if child_left_idx <= N:
            tree[i][0] = child_left_idx
        if child_right_idx <= N:
            tree[i][1] = child_right_idx

    in_order(1)
    num = [0] + num

    print('#{} {} {}'.format(test_case, num.index(1), num.index(N//2)))

