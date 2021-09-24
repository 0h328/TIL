import sys

sys.stdin = open('input.txt')


def in_order(t):
    global result
    if len(tree[t]) >= 3:
        in_order(int(tree[t][2]))
    result += tree[t][1]
    if len(tree[t]) >= 4:
        in_order(int(tree[t][3]))

T = 10

for t in range(1, T + 1):
    N = int(input())
    tree = [0] + [input().split() for _ in range(N)]
    result = ''
    print(tree)

    in_order(1)

    print('#{} {}'.format(t, result))
