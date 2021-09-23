def traverse(node):
    if node == 0:                   # 공백 노드 (단말노드에서 공백노드로) 0을 return
        return 0

    # v로 하는 전체 서브s 트리의 루트 개수를 구할 때
    # 왼쪽 자식을 루트로 하는 서브트리의 개수를 구하기
    # 오른쪽 자식을 루트로 하는 서브트리의 개수를 구하기
    l = traverse(left_child[node])
    r = traverse(right_child[node])
    return l + r + 1                # 왼쪽과 오른쪽 노드의 합을 더한 다음 자기 자신(1)을 더하자

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())    # E(간선의 수), N(루트 노드)
    V = E + 1                           # 정점 = 간선 + 1
    left_child = [0] * (V+1)
    right_child = [0] * (V+1)
    parent = [0] * (V+1)
    temp = list(map(int, input().split()))

    for i in range(0, len(temp), 2):
        p, c = temp[i], temp[i+1]       # temp[i] -> 부모 / temp[i+1] -> 자식
        if left_child[p]:
            right_child[p] = c
        else:
            left_child[p] = c
        parent[c] = p
    ans = traverse(N)
    print('#{} {}'.format(tc, ans))