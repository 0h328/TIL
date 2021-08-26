from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(S):
    global result
    que = deque()
    que.append(S)
    visited[S] = 1  # 시작 방문.
    while que:
        node = que.popleft()
        if node == G: # 현재 지점 도착 노드인 경우 # sum 하게 되는 경우 전체 연결 노드 개수 출력..
            result = visited[node] - 1
            return result
        for i in adj[node]:
            if visited[i] == 0: # 방문하지 않고 갈 수 있는 길
                que.append(i)
                visited[i] = visited[node] + 1 # 이전 방문에 + 1
    return result

for tc in range(int(input())):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for i in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)
    S, G = map(int, input().split())
    visited = [0 for _ in range(V + 1)]
    result = 0  # 연결 안된 경우도 판단~~!!~~!!
    # print(V, E, adj, S, G)
    # print(adj)
    print('#{} {}'.format(tc+1, bfs(S)))