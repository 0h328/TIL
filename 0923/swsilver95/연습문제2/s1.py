import sys
sys.stdin = open('input.txt')

V = int(input())
edges = list(map(int, input().split()))
tree = [[0, 0, 0] for _ in range(V + 1)]

for i in range(V - 1):
    parent, child = edges[i*2], edges[i*2+1]
    if tree[parent][0] == 0:
        tree[parent][0] = child
    else:
        tree[parent][1] = child
    tree[child][2] = parent


# 전위 순회 (V -> L -> R)
def pre_order(node):
    if node:
        print(node, end=' ')
        pre_order(tree[node][0])
        pre_order(tree[node][1])


# 중위 순회 (L -> V -> R)
def in_order(node):
    if node:
        pre_order(tree[node][0])
        print(node, end=' ')
        pre_order(tree[node][1])


# 후위 순회 (L -> R -> V)
def post_order(node):
    if node:
        pre_order(tree[node][0])
        pre_order(tree[node][1])
        print(node, end=' ')


print('전위 순회 : ', end='')
pre_order(1)
print()

print('중위 순회 : ', end='')
in_order(1)
print()

print('후위 순회 : ', end='')
post_order(1)
print()