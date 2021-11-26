import sys
sys.stdin = open('input.txt')


# 전위 순회 (V -> L -> R)
def pre_order(node):
    global cnt
    if node:
        cnt += 1
        print('{}'.format(node), end=' ')
        pre_order(tree[node][0])
        pre_order(tree[node][1])


# 중위 순회 (L -> V -> R)
def in_order(node):
    global cnt
    if node:
        in_order(tree[node][0])
        cnt += 1
        print('{}'.format(node), end=' ')
        in_order(tree[node][1])


# 후위 순회 (L -> R -> V)
def post_order(node):
    global cnt
    if node:
        in_order(tree[node][0])
        in_order(tree[node][1])
        cnt += 1
        print('{}'.format(node), end=' ')


V = int(input())
arr = list(map(int, input().split()))
tree = [[0]*3 for _ in range(V+1)]
cnt = 0

for i in range(V-1):
    parent, child = arr[i*2], arr[i*2+1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child
    tree[child][2] = parent

print('전위 순회')
pre_order(1)
print('', '중위 순회', sep='\n')
in_order(1)
print('', '후위 순회', sep='\n')
post_order(1)