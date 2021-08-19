# 인접 행렬 - 반복

def dfs(v):
    stack = [v]                # 시작 정점 stack에 넣어놓고 시작
    while stack:               # stack이 빌때까지 while len(stack) 등도 가능
        v = stack.pop()        # stack의 가장 위에서 정점을 꺼내 (stack의 가장 위에서 pop)
        if not visited[v]:     # 아직 방문하지 않았다면
            visited[v] = 1     # 방문 체크
            print('방문 정점: {}, 방문 체크: {}'.format(v, visited))
            for w in range(1, V+1):                     # 모든 정점에 대한 반복을 수행하며
                if G[v][w] == 1 and not visited[w]:     # 해당의 인접 정점이고 아직 방문하지 않았다면
                    stack.append(w)                     # stack에 push

from pandas import DataFrame
import sys
sys.stdin = open('input.txt')

# 정점 & 간선
V, E = map(int, input().split())                   # V(ertex): 정점 / E(dge): 간선

# 정점 연결 정보
temp = list(map(int, input().split()))             # 정점에 대한 연결 정보

# V+1 -> 정점을 방문할 때 인덱스 == 정점 번호로 맞추기 위함
G = [[0 for _ in range(V+1)] for _ in range(V+1)]  # 그래프 초기화 (인덱스 관리를 쉽게하기 위해 V+1)
visited = [0 for _ in range(V+1)]                  # 방문 체크 (인덱스 관리를 쉽게하기 위해 V+1)

# 그래프 초기화
for i in range(E):                                 # 무방향 그래프
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1

dfs(1)                                             # 1번 정점부터 dfs 탐색 시작
print(DataFrame(G))