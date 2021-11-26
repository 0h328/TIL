def bfs(start):                                       # 나로 부터 만들 수 있는 모든 친구 관계 생성
    Q = [start]
    pairs[start] = 1                                  # 팀을 맺음

    while Q:
        cur = Q.pop(0)
        for w in range(1, V+1):                       # 전체 학생을 체크하며 나와 이어진 모든 학생을 확인
            if not pairs[w] and G[cur][w]:            # 만약 아직 팀이 맺어지지 않았고 나와 연결되어 있다면(== 인접 정점이라면)
                pairs[w] = 1                          # 팀을 맺고
                Q.append(w)                           # w로 인해 새롭게 팀이 구성될 수 있기 때문에 Q에 넣자
                                                      # ex. 1번으로부터 만들 수 있는 팀을 모두 만들기

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())                  # N(V): 정점 / M(E): 간선 -> 바꿔서 표현
    pairs = [0] * (V+1)                               # 팀을 맺었는지 여부를 체크하기 위한 배열
    edge = list(map(int, input().split()))            # 간선 정보
    # G = [[0] * (V+1) for _ in range(V+1)]
    G = [[0 for _ in range(V+1)] for _ in range(V+1)] # 인접 행렬

    """
    인접 행렬에 표시하는 다른 방법
    for i in range(0, len(edge), 2):
        A = edge[i]; B = edge[i+1]
        G[A][B] = G[B][A] = 1
    """
    for i in range(E):                                # 인접 행렬에 표시
        A = edge[i*2]; B = edge[i*2+1]
        G[A][B] = G[B][A] = 1

    ans = 0                  #                         페어수 확인
    for i in range(1, V+1):                           # 전체 학생을 돌면서 팀을 맺었는지 여부 확인
        if not pairs[i]:                              # 아직 팀이 없다면
            ans += 1                                  # 한 팀 증가
            bfs(i)                                    # bfs 탐색

    print('#{} {}'.format(tc, ans))