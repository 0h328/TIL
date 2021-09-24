import sys
sys.stdin = open('input.txt')

def in_order(n):
    global result
    if len(tree[n]) >= 3:
        in_order(int(tree[n][2]))
    result += tree[n][1]
    if len(tree[n]) >= 4:
        in_order(int(tree[n][3]))

for tc in range(1, 11):
    N = int(input())
    # tree = [0]
    # for _ in range(N):
    #     tree += [input().split()]
    tree = [0] + [input().split() for _ in range(N)]
    result = ''

    in_order(1)

    print('#{} {}'.format(tc, result))