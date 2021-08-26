# pure queue
def bfs(v):
    Q = [0] * V    # 정점 정보를 담기 위한 Queue
    front = rear = -1
    rear += 1      # 시작점 enQueue를 위한 포인터
    Q[rear] = v    # enQueue
    visited[v] = 1 # 방문 처리
    print(*visited)

    while front != rear:   # Queue가 비어있지 않으면
        front += 1         # deQueue를 위한 포인터 생성
        v = Q[front]       # 이후에 deQueue
        for w in range(1, V+1):
            if G[v][w] and not visited[w]:  # v에 인접하고 아직 방문하지 않은 곳이라면
                rear += 1                   # enQueue를 위해 값을 하나 증가 시키고
                Q[rear] = w                 # 해당 위치(rear)에 인접 정점(w)을 추가
                visited[w] = visited[v] + 1 # 방문처리(거리정보) 갱신
                print(*visited)

import sys
sys.stdin = open('input.txt')
# V(ertex), E(dge)
V, E = map(int, input().split())
# 간선 정보 초기화
temp = list(map(int, input().split()))
# Graph 초기화
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(E):
    n1, n2 = temp[2*i], temp[2*i+1]
    G[n1][n2] = 1
    G[n2][n1] = 1
# 방문 표시 초기화
visited = [0] * (V+1)
# bfs 탐색 시작
bfs(1)