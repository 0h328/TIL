import sys
sys.stdin = open('input.txt')

# 소요시간 32분50초

# thought process:5분
# 원하는 답: 1번 노드의 연결된 모든 노드 출력
# 프로세스: dfs 와 bfs 둘 다 사용 가능
#   => 리스트 활용해서 dfs 먼저 풀이

# 11분 58초
def bfs(v):
    Q = [v]
    while Q:
        v = Q.pop(0)
        if G[v]:
            for j in G[v]:
                if not visited[j]:
                    visited[j] = 1
                    Q.append(j)
                    ans.append(j)
    return len(ans)

# 20분 52초
def dfs(v):
    if G[v]:
        for j in G[v]:
            if not visited[j]:
                visited[j] = 1
                ans.append(j)
                dfs(j)
    return len(ans)


N = int(input())
E = int(input())
arr = [list(map(int, input().split())) for _ in range(E)]
G = [[] for _ in range(E+1)]
visited = [0] * (N+1)
ans = []
for i in range(E):
    G[arr[i][0]].append(arr[i][1])

print(bfs(1))
visited = [0] * (N+1)
ans = []
print(dfs(1))
