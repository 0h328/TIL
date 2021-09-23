'''
정점이 단순한 수이면 정점번호와 해당 양의 정수가 주어지고,
정점이 연산자이면 정점번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점번호가 차례대로 주어진다.
계산을 보아하니, 중위순회~!
'''

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())

    tree = [[0 for _ in range(4)] for _ in range(N + 1)]  # 끝에 value 칸 삽입! (range(4)) / 좌자식, 우자식, 부모, 값

    for i in range(N):
        node_info = list(input().split())

        if len(node_info) == 4:
            tree[int(node_info[0])][3] = node_info[1]
            tree[int(node_info[0])][0] = node_info[2]
            tree[int(node_info[0])][1] = node_info[3]
            tree[int(node_info[2])][2] = node_info[0]
            tree[int(node_info[3])][2] = node_info[0]

        else:
            tree[int(node_info[0])][3] = node_info[1]

    while

    print('#{} {}'.format(tc, tree))