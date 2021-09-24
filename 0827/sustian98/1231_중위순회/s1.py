import sys
sys.stdin = open('input.txt')

def inorder(i):
    global s
    # if i <= n:
    if len(tree[i]) > 2:
        inorder(int(tree[i][2]))
    s += tree[i][1]
    if len(tree[i]) > 3:
        inorder(int(tree[i][3]))

for idx in range(1, 11):
    n = int(input())
    s = ''
    tree = [[]] + [input().split() for _ in range(n)]
    inorder(1)
    print('#{} {}'.format(idx, s))
