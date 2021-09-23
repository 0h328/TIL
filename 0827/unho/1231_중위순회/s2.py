'''
0923
'''


import sys
sys.stdin = open('input.txt')


def in_order(node):                     # 중위순회
    if len(tree[node]) > 2:
        in_order(int(tree[node][2]))

    answer.append(tree[node][1])

    if len(tree[node]) > 3:
        in_order(int(tree[node][3]))


for tc in range(1, 11):
    N = int(input())
    tree = [[]]
    answer = []

    for _ in range(N):
        tree.append(input().split())
    print(tree)

    in_order(1)

    print('#{} {}'.format(tc, ''.join(answer)))