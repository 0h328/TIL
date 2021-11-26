from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input())

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        cur = queue.popleft()
        for nxt in G[cur]:      # 인접 리스트 접근
            if nxt == end:
                return visited[cur]     # 시작점을 1로 두고 계산했으므로 nxt까지의 거리에서 1을 뺀 cur 좌표까지의 거리 return
            if not visited[nxt]:
                visited[nxt] = visited[cur] + 1
                queue.append(nxt)
    return 0                    # while 다 돈 경우, 목적지에 도착할 수 없으므로 return 0

for tc in range(1, T+1):
    V, E = map(int, input().split())

    # G = [[] for _ in range(V+1)]        # 인접 리스트
    # for _ in range(E):
    #     node1, node2 = map(int, input().split())
    #     G[node1].append(node2)
    #     G[node2].append(node1)
    G = {i: [] for i in range(V+1)}         # 인접 딕셔너리
    for _ in range(E):
        node1, node2 = map(int, input().split())
        G[node1].append(node2)
        G[node2].append(node1)

    start, end = map(int, input().split())

    visited = [0 for _ in range(V+1)]

    print('#{} {}'.format(tc, bfs(start)))