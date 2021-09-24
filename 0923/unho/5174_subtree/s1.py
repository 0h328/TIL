import sys
sys.stdin = open('input.txt')


def pre_order(node):                                    # 전위 순회
    global answer

    if not node:
        return

    answer += 1

    pre_order(tree[node][0])
    pre_order(tree[node][1])


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    n_list = list(map(int, input().split()))

    tree = [[0]*3 for _ in range(E+2)]                      # 왼쪽 자식 / 오른쪽 자식 / 부모
    answer = 0

    for idx in range(E):                                    # 노드간 관계 정리
        parent, child = n_list[idx*2], n_list[idx*2 + 1]

        if not tree[parent][0]:                             # 왼쪽 노드 비어 있으면 왼쪽으로
            tree[parent][0] = child
        else:                                               # 왼쪽 노드에 있으면 오른쪽으로
            tree[parent][1] = child

        tree[child][2] = parent                             # 자식노드의 부모노드 칸에 부모 내용 추가

    pre_order(N)

    print('#{} {}'.format(tc, answer))