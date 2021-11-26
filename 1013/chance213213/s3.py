'''
경로에는 같은 정점의 번호가 2번 이상 등장할 수 없으며
'''
import sys
sys.stdin = open('input.txt')

def solve(v):
    global result
    if max(visited) > result:
        result = max(visited)
    visited[v] += 1
    for w in G2[v]:
        if not visited[w]:
            solve(w)
            visit.append(w)
            # visited[w] -= 1
def dfs(v):
    global result

    if not visited[v]:
        visited[v] = 1

    if max(visited) > result:
        result = max(visited)

    for w in range(N+1):
        if G[v][w] == 1 and not visited[w]:
            temp_w = visited[w]
            visited[w] = visited[v] + 1
            dfs(w)
            visited[w] = temp_w

T = int(input()) #2

for tc in range(1, T+1):
    N, M = map(int, input().split())    #N개의 정점, M개의 간선
    temp = [list(map(int, input().split())) for _ in range(M)]
    G = [[0] * (N+1) for _ in range(N+1)]
     #0번도 사용하기
    visit = []
    for i in range(len(temp)):
        G[temp[i][0]][temp[i][1]] = 1
        G[temp[i][1]][temp[i][0]] = 1
    G2 = [[] for _ in range(N+1)]
    for i in range(len(temp)):
        G2[temp[i][0]].append(temp[i][1])
        G2[temp[i][1]].append(temp[i][0])
    result = 0
    for v in range(N+1):
        visited = [0] * (N + 1)
        dfs(v)
    # print(visited)
    print('#{} {}'.format(tc, result))
