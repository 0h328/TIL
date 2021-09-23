import sys
sys.stdin = open('input.txt')

def in_order_tree(node):
    global num
    if node <= N:
        in_order_tree(node * 2)
        tree[node] = num
        num += 1
        in_order_tree(node * 2 + 1)
        return tree


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    num = 1
    in_order_tree(1)

    print('#{0} {1} {2}'.format(tc, tree[1], tree[N // 2]))
