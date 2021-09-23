import sys

sys.stdin = open('input.txt')


def post_order(t):
    if len(tree[t]) >= 3:
        a = post_order(int(tree[t][2]))
    if len(tree[t]) >= 4:
        b = post_order(int(tree[t][3]))
    m = tree[t][1]
    if m.isdigit():
        return m
    else:
        return str(eval(a + m + b))

for t in range(1, 11):
    N = int(input())

    tree = [0] + [input().split() for _ in range(N)]
    result = [0] * (N + 1)

    print('#{} {}'.format(t, int(float(post_order(1)))))