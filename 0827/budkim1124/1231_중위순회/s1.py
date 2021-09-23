import sys
sys.stdin = open('input.txt')


def in_order(v):
    if v <= N:
        in_order(v*2)
        print(tree[v], end='')
        in_order(v*2+1)

for t in range(10):
    N = int(input())
    tree = [0] * (N+1)
    for i in range(N):
        root = input().split()
        tree[int(root[0])] = root[1]

    print('#{} '.format(t+1), end=' ')
    in_order(1)
    print()


