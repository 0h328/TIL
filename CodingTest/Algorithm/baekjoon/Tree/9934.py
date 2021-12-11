import sys
sys.stdin = open('input.txt')

K = int(input())
data = list(map(int, input().split()))
tree = [[] for _ in range(K)]

def pre_order(node, idx):
    mid = (len(node)//2)
    tree[idx].append(node[mid])
    if len(node) == 1:
        return
    pre_order(node[:mid], idx+1)
    pre_order(node[mid+1:], idx+1)

pre_order(data, 0)
for i in range(K):
    print(*tree[i])