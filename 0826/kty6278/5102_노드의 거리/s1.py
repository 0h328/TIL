from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(S):
    que = deque()
    que.append(S)
    while que:
        node = que.popleft()
        if node == G: # 현재 지점 도착 노드인 경우
            return visited[node]
        for i in adj[node]:
            if visited[i] == 0: # 방문하지 않은 길
                que.append(i)
                visited[i] = visited[node] + 1 # 이전 방문에 + 1
    return 0

for tc in range(int(input())):
    V, E = map(int, input().split())
    adj = [[] * (V+1) for i in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)
    S, G = map(int, input().split())
    visited = [0 for _ in range(V + 1)]
    print('#{} {}'.format(tc+1, bfs(S)))