import sys
sys.stdin = open('input.txt')


def pre_order(node):
    global answer_cnt
    if not node:                # 노드가 없으면 종료
        return

    answer_cnt += 1
    pre_order(linked[node][0])
    pre_order(linked[node][1])


T = int(input())

for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    n1_parents = []
    answer_node, answer_cnt = 0, 0

    li = list(map(int, input().split()))
    linked = {}

    for idx in range(E):                            # 노드 연결 관계 설정
        if not linked.get(li[idx*2]):               # 키가 없으면 값을 [0, 0, 0] 으로 초기화 / 왼쪽 자식, 오른쪽 자식, 부모
            linked[li[idx*2]] = [0, 0, 0]

        if not linked[li[idx*2]][0]:                # 왼쪽 자식이 비어있으면 왼쪽에 추가
            linked[li[idx*2]][0] = li[idx*2 + 1]
        else:                                       # 왼쪽 자식 있으면 오른쪽에 추가
            linked[li[idx*2]][1] = li[idx*2 + 1]

        if not linked.get(li[idx*2 + 1]):           # 자식 키가 없으면 [0, 0, 0] 으로 초기화
            linked[li[idx*2 + 1]] = [0, 0, 0]
        linked[li[idx*2 + 1]][2] = li[idx*2]        # 자식 데이터에도 부모 데이터 추가

    # print('LOG --- LINKED SETTINGS\n{}'.format(linked))

    parent = linked[n1][2]              # 첫번째 노드의 부모 노드들 모두 구함
    while parent:
        n1_parents.append(parent)
        parent = linked[parent][2]

    parent = linked[n2][2]              # 두번째 노드의 부모가 첫번째 부모 모임에 있으면 탈출
    while parent not in n1_parents:
        parent = linked[parent][2]
    answer_node = parent                # 가장 빨리 겹치는 부모 노드 발견시 정답 0번째 인덱스에 저장

    # print('LOG --- INTERSECT PARENT ANSWER : {}'.format(answer_node))

    pre_order(answer_node)              # 서브 루트 카운트

    print('#{} {} {}'.format(tc, answer_node, answer_cnt))