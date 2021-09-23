import sys
sys.stdin = open('input.txt')


def subtree(node):
    global node_cnt
    if tree[node]:
        node_cnt += 1
        if tree[node][0]:
            subtree(tree[node][0])
        if tree[node][1]:
            subtree(tree[node][1])


T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    tree = [[0 for _ in range(3)] for _ in range(E+2)]
    temp = list(map(int, input().split()))

    for i in range(E): # 트리 만들기
        parent, child = temp[i * 2], temp[i * 2 + 1]
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        tree[child][2] = parent

    node_cnt = 0
    subtree(N)

    print('#{} {}'.format(t, node_cnt))