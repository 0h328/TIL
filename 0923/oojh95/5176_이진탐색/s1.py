import sys
sys.stdin = open('input.txt')


def in_order(node):
    global cnt
    if node != 0 and node < N+1:
        in_order(tree[node][0])             # 왼쪽
        tree[node][2] = cnt   # 노드
        cnt += 1
        in_order(tree[node][1])             # 오른쪽


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [[0 for _ in range(3)] for _ in range(N+1)]

    for i in range(1, N+1):
        tree[i][0] = i * 2
        tree[i][1] = i * 2 + 1

    cnt = 1
    in_order(1)
    print('#{} {} {}'.format(tc, tree[1][2], tree[N//2][2]))
