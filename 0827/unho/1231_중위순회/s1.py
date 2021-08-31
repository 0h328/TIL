import sys
sys.stdin = open('input.txt')



def in_order(node):
    if len(binary_tree[node]) >= 3:
        in_order(int(binary_tree[node][2]))

    answer.append(binary_tree[node][1])

    if len(binary_tree[node]) >= 4:
        in_order(int(binary_tree[node][3]))

for tc in range(1, 11):
    N = int(input())
    binary_tree = [[]]
    answer = []

    for _ in range(N):
        binary_tree.append(input().split())

    in_order(1)

    print('#{} {}'.format(tc, ''.join(answer)))