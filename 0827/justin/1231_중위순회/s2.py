def in_order(node):
    if node != 0:
        in_order(tree[node][0])
        print(tree[node][3], end='')
        in_order(tree[node][1])

import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    V = int(input())                            # N보단 V
    tree = [[0, 0, 0, ''] for _ in range(V+1)]  # LC, RC, PA, ALPHA
    for _ in range(V):                          # 정점 수만큼 돌며 정보를 받아
        temp = input().split()                  # 노드, 알파벳, 왼쪽 자식, 오른쪽 자식
        node, alpha = int(temp[0]), temp[1]
        for i in range(2, len(temp)):           # 트리 정보 초기화 -> 왼쪽(+오른쪽) 노드
            tree[node][i-2] = int(temp[i])
            tree[int(temp[i])][2] = node
        tree[node][3] = alpha                   # 부모 -> 알파벳
    print('#{}'.format(tc), end=' ')
    in_order(1)
    print()