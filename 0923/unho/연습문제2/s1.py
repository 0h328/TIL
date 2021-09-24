# 전위 순회 (V -> L -> R)
def pre_order(node):
    pass

# 중위 순회 (L -> V -> R)
def in_order(node):
    pass

# 후위 순회 (L -> R -> V)
def post_order(node):
    pass



import sys
sys.stdin = open('input.txt')


V = int(input())
n_list = list(map(int, input().split()))
tree = [[0]*3 for _ in range(V+1)]

for idx in range(V-1):
    parent, child = n_list[2*idx], n_list[2*idx+1]

    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child

    tree[child][2] = parent

print(tree)

print('전위 순회 : ', end='')
pre_order(1)
print()

print('중위 순회 : ', end='')
in_order(1)
print()

print('후위 순회 : ', end='')
post_order(1)
print()