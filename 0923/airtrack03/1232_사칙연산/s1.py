import sys
sys.stdin = open('input.txt')

T = 10

def calc_tree(node):
    left_node = tree[node][1]
    right_node = tree[node][2]

    if left_node and not tree[left_node][0].isdigit():
        calc_tree(left_node)
    if right_node and not tree[right_node][0].isdigit():
        calc_tree(right_node)

    if left_node and right_node:
        expression = tree[left_node][0] + tree[node][0] + tree[right_node][0]
        tree[node][0] = str(eval(expression))



for tc in range(1, T+1):
    N = int(input())

    tree = [[0] * 3 for _ in range(N+1)]

    for _ in range(N):
        left, right = 0, 0

        data = input().split()
        node = int(data[0])
        value = data[1]

        if len(data) > 2:
            left = int(data[2])
        if len(data) > 3:
            right = int(data[3])

        tree[node][0] = value
        tree[node][1] = left
        tree[node][2] = right

    root = 1
    calc_tree(root)
    ans = tree[root][0].split('.')[0]

    print('#{} {}'.format(tc, ans))