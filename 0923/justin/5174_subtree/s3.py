import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())    # E(간선의 수), N(루트 노드)
    V = E + 1                           # 정점 = 간선 + 1
    left_child = [0] * (V+1)            # 정점 번호를 인덱스로 활용
    right_child = [0] * (V+1)
    parent = [0] * (V+1)
    temp = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        p, c = temp[i], temp[i+1]     # temp[i] -> 부모 / temp[i+1] -> 자식
        if left_child[p]:
            right_child[p] = c
        else:
            left_child[p] = c
        parent[c] = p

    ans = 0
    Q = [N]                       # 서브 트리의 시작점을 Q에 넣고
    while Q:
        v = Q.pop(0)              # 큐에서 정점 정보를 하나 꺼내서
        if v == 0:                # 그 값이 0이면? 공백 노드!(단말 노드, 리프 노드) -> 넘어가자
            continue
        ans += 1                  # 공백 노드인 경우는 continue를 통해서 반복을 뛰어넘기 때문에 카운팅 x
        Q.append(left_child[v])   # Q에 들어가는 개수만큼 노드 수
        Q.append(right_child[v])

    print('#{} {}'.format(tc, ans))