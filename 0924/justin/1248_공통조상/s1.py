# 부모 & 조상 찾기
def search_ance(n):
    s = tree[n][2]      # n번 노드의 부모
    p = []
    while s != 0:       # 루트 노드를 만나기 전까지 (루트 노드는 부모가 0)
        p.append(s)     # 해당 부모 노드를 리스트에 넣고
        s = tree[s][2]  # 그 부모 노드의 부모를 찾아 s에 다시 할당
    return p            # p는 n의 부모부터 조상 노드가 순서대로 들어있음

# p1과 p2의 공통 조상 찾기
def find_common_ance(p1, p2):
    for i in range(len(p1)):
        for j in range(len(p2)):
            if p1[i] == p2[j]:
                return p1[i]
    return 0

# 공통 조상을 찾아 순회(전/중/후위 순회 관계 x)
def pre_order(node):
    global cnt
    if node != 0:
        cnt += 1
        pre_order(tree[node][0])
        pre_order(tree[node][1])


import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())                # V, E, 공통 조상을 찾는 2개의 정점 번호(n1, n2)
    tree = [[0 for _ in range(3)] for _ in range(V + 1)]    # left, right, parent
    temp = list(map(int, input().split()))                  # 정점 연결 정보
    p1, p2 = [], []
    cnt = 0
    for i in range(E):
        parent = temp[i*2]
        child = temp[i*2+1]
        if not tree[parent][0]:                             # 부모 노드의 왼쪽 자식이 없으면 왼쪽 자식으로 추가
            tree[parent][0] = child
        else:                                               # 부모 노드의 왼쪽 자식이 있으면 오른쪽 자식으로 추가
            tree[parent][1] = child
        tree[child][2] = parent                             # 부모 노드도 초기화
    p1 = search_ance(n1)                                    # n1과 n2의 조상을 찾아 반환
    p2 = search_ance(n2)
    common_ance = find_common_ance(p1, p2)                  # 공통 조상 찾기
    pre_order(common_ance)                                  # 순회 돌면서 cnt값
    print('#{} {} {}'.format(tc, common_ance, cnt))         # 공통 조상 중 가장 가까운 것의 번호 / common_ance를 루트로 하는 서브 트리의 크기