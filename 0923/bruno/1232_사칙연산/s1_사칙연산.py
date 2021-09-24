import sys
sys.stdin = open('input.txt')


def post_order(t):

    if len(tree[t]) == 4:
        post_order(int(tree[t][2]))
        post_order(int(tree[t][3]))

    if tree[t][1] == '+':
        tree[t][1] = int(tree[int(tree[t][2])][1]) + int(tree[int(tree[t][3])][1])
    elif tree[t][1] == '-':
        tree[t][1] = int(tree[int(tree[t][2])][1]) - int(tree[int(tree[t][3])][1])
    elif tree[t][1] == '*':
        tree[t][1] = int(tree[int(tree[t][2])][1]) * int(tree[int(tree[t][3])][1])
    elif tree[t][1] == '/':
        tree[t][1] = int(tree[int(tree[t][2])][1]) / int(tree[int(tree[t][3])][1])


for tc in range(1, 11):
    N = int(input())
    tree = [0] + [input().split() for _ in range(N)]

    post_order(1)

    print('#{} {}'.format(tc, int(tree[1][1])))
