import sys
sys.stdin = open('input.txt')
V = int(input())
E = V - 1

tree = [list(for [0] in range(3)) for _ in range(V+1)]
temp = list(map(int, input().split()))


cnt = 0
for i in range(E):
    parent, child = temp[i*2], temp[i*2+1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child
    tree[parent][2] = parent
