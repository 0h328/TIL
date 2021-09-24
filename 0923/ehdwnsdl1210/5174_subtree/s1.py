def pre_order(node):
    global cnt
    if node != 0:
        cnt += 1                           # 방문한 정점의 개수 체크
        # print('{}'.format(node), end=' ')  # 노드 / 출력 아할꺼니까 필요 X
        pre_order(tree[node][0])           # 왼쪽
        pre_order(tree[node][1])           # 오른쪽

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())

    temp = list(map(int, input().split()))

    tree = [[0 for _ in range(3)] for _ in range(max(temp) + 1)]    # 숫자가 순차적이지 않아서 최대값을 기준으로, 인덱스할꺼니까

    cnt = 0

    for i in range(E):                                      # 간선의 수만큼 반복을 돌며
        parent, child = temp[i * 2], temp[i * 2 + 1]
        if not tree[parent][0]:                             # parent 노드의 왼쪽 자식이 없다면
            tree[parent][0] = child                         # 왼쪽 자식으로 넣고
        else:                                               # parent 노드의 왼쪽 자식이 있다면
            tree[parent][1] = child                         # 오른쪽 자식으로 넣자
        tree[child][2] = parent                             # 이후 부모 노드 초기화

    pre_order(N)    # 주어진 N의 sub tree를 찾는거니까

    print('#{} {}'.format(tc, cnt))