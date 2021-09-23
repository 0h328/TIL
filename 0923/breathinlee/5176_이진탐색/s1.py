import sys
sys.stdin = open('input.txt')

# 왼쪽 자식 < 부모 < 오른쪽 자식
def in_order(node):
    if node != 0:
        in_order(tree[node][1])
        in_order_list.append(node)
        in_order(tree[node][2])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [[0] * 3 for _ in range(N+1)]
    in_order_list = []
    for i in range(N+1):
        tree[i][0] = i
        if N % 2:
            for j in range(1, N//2+1):
                tree[j][1] = 2 * j
                tree[j][2] = 2 * j + 1
        else:
            for j in range(1, N//2):
                tree[j][1] = 2 * j
                tree[j][2] = 2 * j + 1
            tree[j+1][1] = N


    in_order(1)

    a = in_order_list.index(1) + 1
    b = in_order_list.index(N//2) + 1
    print('#{} {} {}'.format(tc, a, b))




