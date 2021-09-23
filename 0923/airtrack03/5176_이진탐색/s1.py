import sys
sys.stdin = open('input.txt')

T = int(input())

def make_tree(node):
    global count

    if node <= N:
        make_tree(node*2)

        tree[node] = count
        count += 1

        make_tree(node*2 + 1)


for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N + 1)

    count = 1
    make_tree(1)

    root = tree[1]
    ans = tree[N//2]

    print('#{} {} {}'.format(tc, root, ans))







