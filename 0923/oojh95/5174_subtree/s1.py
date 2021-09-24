def pre_order(node):
    global cnt
    if node != 0:
        cnt += 1    # 노드 갯수를 세는데 전위순회로 세도록 구현
        pre_order(tree[node][0])
        pre_order(tree[node][1])


import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split())) # 간선정보 입력받음
    tree = [[0 for _ in range(3)] for _ in range(E + 2)]
    cnt = 0 # 결국은 구하고자 하는 정답 노드의 갯수 초기화
    for i in range(E):  # 간선정보에 따른 트리 구현
        parent, child = temp[i*2], temp[i*2+1]
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        tree[child][2] = parent
    pre_order(N)    # 전위 순회 사용
    print('#{} {}'.format(tc, cnt))