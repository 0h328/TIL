import sys

sys.stdin = open('input.txt')

def find_num(node):
    if node > N:
        return 0
    if tree[node]:
        return tree[node]
    l = node * 2
    r = l + 1

    tree[node] = find_num(l) + find_num(r)

    return(tree[node])

T = int(input())

for i in range(T):
    N, M, L = map(int,input().split())
    tree = [0 for _ in range(N+1)]
    for k in range(M):
        n, v = map(int,input().split())
        tree[n] = v
    print('#{} {}'.format(i+1,find_num(L)))