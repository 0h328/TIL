def post_order(v):             # 후위 순회
    if v > N:                  # 유효한 노드가 아니면 0 반환
        return 0
    if tree[v] != 0:           # 리프 노드인 경우
        return tree[v]         # 저장된 값 반환

    l = post_order(2*v)        # 왼쪽 자식으로 이동
    r = post_order(2*v+1)      # 오른쪽 자식으로 이동
    tree[v] = l + r            # 양쪽의 값을 더해서 저장
    return tree[v]             # 노드에 저장된 값을 반환

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for i in range(N+1)]
    for i in range(M):
        idx, value = map(int, input().split())  # 리프 노드 값을 입력받아 저장
        tree[idx] = value
    post_order(1)
    ans = tree[L]
    print('#{} {}'.format(tc, ans))
