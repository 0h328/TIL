def traverse(node):
    global ans
    # 노드가 0인 경우는 종료 혹은 조건 분기
    # if v == 0: return

    # 카운팅 위치는 관계없음 (거쳐가는 세 번의 시점 중 한번만 체크하면 됨)
    if node != 0:
        # ans += 1
        traverse(left_child[node])
        # ans += 1
        traverse(right_child[node])
        # 노드 개수 확인
        ans += 1

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())        # E(간선의 수), N(Subtree의 기준이 되는 루트 노드)
    V = E + 1                               # V = E + 1(정점 = 간선 + 1)
    left_child = [0] * (V+1)                # 왼쪽 자식
    right_child = [0] * (V+1)               # 오른쪽 자식
    parent = [0] * (V+1)                    # 부모
    temp = list(map(int, input().split()))  # 들어오는 노드 정보(부모 - 자식)

    for i in range(0, len(temp), 2):
        p, c = temp[i], temp[i+1]           # temp 배열에 저장된 값은 들어오는 순서(부모 - 자식)가 고정
                                            # 부모 노드를 인덱스로 하여 자식 노드 번호를 저장
        if left_child[p]:                   # 왼쪽 자식이 있으면
            right_child[p] = c              # 오른쪽 자식 추가
        else:                               # 왼쪽 자식이 없다면
            left_child[p] = c               # 왼쪽 자식으로 채우자
        parent[c] = p                       # 자식에서 부모 정보를 채웠으면 부모 입장에서 어떤 자식과 연결되어 있는지 체크 필요
    ans = 0                                 # 몇 개의 노드를 거치는지 확인하기 위한 변수
    traverse(N)                             # 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수 (루트에서만 순회를 시작해야 하는 것은 아님)
    print('#{} {}'.format(tc, ans))