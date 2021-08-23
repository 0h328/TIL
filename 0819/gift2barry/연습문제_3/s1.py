"""
1. dfs - 인접 행렬 - 반복
"""

def dfs(v):
    # 스택 자료구조 이용한 방법
    # stack = [v]     # 시작 정점을 stack에 넣고시작하자
    #
    # while stack:    # 모든 정점을 방문할때까지 반복
    #     v = stack.pop()
    #
    #     if not visited[v]:  # 아직 방문 안한 정점이면
    #         visited[v] = 1  # 방문체크!
    #         print('방문정점: {}, 방문체크: {}'.format(v, visited))
    #
    #         for w in range(1, V+1):     # 1번노드로부터 방문 가능한 노드를 다 확인 (첫번쨰 인덱스는 더미니까 1 부터 루프)
    #             if G[v][w] == 1 and not visited[w]:     # v의 인접 정점(w) 이고 그곳을 아직 방문 안했으면,
    #                 stack.append(w)                     # 해당 정점을 스택에 추가!

    # 재귀 활용한 방법
    if not visited[v]:    # 해당정점에 이미 방문했는지를 확인
        visited[v] = 1    # 방문 안했으면 방문체크!
    for w in range(1, V+1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))
print(temp)
# Graph 초기화
G = [[0 for _ in range(V+1)]for _ in range(V+1)]    # 정점보다 하나 더많으니까 V + 1

# 그래프에 노드 숫자 입력하기
# 인접행렬 표현식!
# for i in range(E):   # edge 개수만큼 반복
#     G[temp[i*2]][temp[i*2+1]] = 1
#     G[temp[i*2+1]][temp[i*2]] = 1
# print(G)

# 인접 리스트 표현식!
# 인덱스 0 이 빈 리스트값인 이유는, 인덱스번호와 숫자 와 위치 맞추기위한 더미데이터!
G = [[] for _ in range(V+1)]
for i in range(1, len(temp), 2):
    G[temp[i-1]].append(temp[i])
    G[temp[i]].append(temp[i-1])
print(G)

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]   # 인덱스번호와 숫자 위치 맞추기위한 더미데이터위해 V + 1
print(visited)

# dfs 탐색 시작
dfs(1)  #1번 정점부터 탐색하기 시작한다는 뜻, dfs(2)는 2번정점부터 탐색한다는 뜻