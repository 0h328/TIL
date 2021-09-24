import sys
sys.stdin = open('input.txt')

def in_order(root):
    if root <= n:
        in_order(root*2)
        print(*tree[root], end = '')
        in_order(root*2+1)

for tc in range(10):
    n = int(input())
    tree = [[] for i in range(n+1)]
    for i in range(n):
        node = list(map(str, input().split()))
        tree[int(node[0])].append(node[1])
    print('#{}'.format(tc + 1), end=' ')
    in_order(1)
    print()

