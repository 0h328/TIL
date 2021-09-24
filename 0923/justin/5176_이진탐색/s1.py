def in_order(v):
    global cnt
    if v > N:               # N은 마지막 값 -> 이것보다 커질 수 없음 (갈곳이 없다면 돌아가기)
        return
                            # 부모 노드를 기준으로 v*2 -> 왼쪽 자식 & v*2+1 -> 오른쪽 자식
    in_order(v*2)           # 왼쪽 서브트리 방문
    # print(v, end=' ')
                            # 4번 노드 방문 시점에 1 저장 -> 2번 노드 방문 시점에 2 저장 -> 5번 노드 방문 시점에 3 저장..
    tree[v] = cnt           # cnt를 v번 노드에 저장
    cnt += 1                # +1 (N까지 증가 예정)
    in_order(v*2+1)         # 오른쪽 서브트리 방문

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())                                    # 1 ~ N번 노드
    tree = [0] * (N+1)                                  # 인덱스 편의를 위해 N+1
    cnt = 1                                             # 1번 노드부터 시작
    in_order(1)                                         # root를 1번으로 시작 -> 트리 정보 구성
    root_node, half_node = tree[1], tree[N//2]          # 구성된 tree 정보로 정답 도출
    print('#{} {} {}'.format(tc, root_node, half_node))