def dfs(v):
    global result
    visited[v] = 1      # 넘겨 받은 시작 정점 방문 체크
    if v == B:          # 만약 해당 정점이 목표 지점이라면
        result = 1      # 갈 수 있으니 1로 바꾸고
        return          # 함수 종료
    for w in range(0, SIZE):                        # 0부터 반복을 돌며
        if G[v][w] == 1 and visited[w] == 0:    # 해당 정점의 인접 정점이고 그 정점에 아직 방문하지 않았으면
            dfs(w)                                  # 방문 처리

import sys
sys.stdin = open('input.txt')
SIZE = 100    # 사이즈 고정 (리스트도 사용 가능)
A = 0         # 시작 지점
B = 99        # 목표 지점

for _ in range(1, 11):
    result = 0                                              # 갈 수 있는지 여부를 체크
    tc, E = map(int, input().split())                       # tc / Edge(간선) - 길의 총 개수
    temp = list(map(int, input().split()))                  # (출발 정점 - 도착 정점) 구조 -> A는 0(출발점) / B는 99(도착점) 고정
    G = [[0 for _ in range(SIZE)] for _ in range(SIZE)]     # 0으로 구성된 2차원 초기화 (100 * 100)
    visited = [0 for i in range(SIZE)]                      # 방문 처리를 위한 리스트 (0번부터 시작하니 굳이 SIZE+1을 하지 않아도 됨)
    for i in range(0, len(temp), 2):                        # 인접 행렬로 체크(방향이 존재하기 때문에 행에 맞는 열(->)만 1로 체크)
        # i -> 0, 2, 4, 6, 8 ...
        """
        G[temp[0][temp[1]]
        G[temp[1][temp[2]]
        G[temp[3][temp[4]]
        ...
        """
        G[temp[i]][temp[i+1]] = 1
    dfs(A)                                                  # (A의 시작점은 0으로 고정) dfs 탐색 시작
    print('#{} {}'.format(tc, result))