import sys
sys.stdin = open('input.txt')

def fill_tree(node):
    global val
    if n >= tree[node][0] > 0:
        fill_tree(tree[node][0])
    tree[node][2] = val
    val += 1
    if n >= tree[node][1] > 0:
        fill_tree(tree[node][1])

t = int(input())
for idx in range(1, t+1):
    n = int(input())
    tree = [[2*i, 2*i + 1, 0] for i in range(n+1)]
    print(tree)
    val = 1
    fill_tree(1)
    print('#{} {} {}'.format(idx, tree[1][2], tree[n//2][2]))