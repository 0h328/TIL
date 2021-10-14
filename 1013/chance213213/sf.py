'''
경로에는 같은 정점의 번호가 2번 이상 등장할 수 없으며
'''
import sys
sys.stdin = open('input.txt')

def dfs(v):
    global result

    # if not visited[v]:
    #     visited[v] = 1

    if max(visited) > result:
        result = max(visited)

    for w in G2[v]:
        if not visited[w]:
            #visited[w] 값을 잠시 담아 놓음
            temp_w = visited[w]
            #이제까지 온 거리를 더하는 것
            visited[w] = visited[v] + 1
            dfs(w)
            #다시 돌아왔을 때, 원래 값으로 돌려 줌
            visited[w] = temp_w

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    #N개의 정점, M개의 간선
    temp = [list(map(int, input().split())) for _ in range(M)]

    G2 = [[] for _ in range(N+1)]

    for i in range(len(temp)):
        G2[temp[i][0]].append(temp[i][1])
        G2[temp[i][1]].append(temp[i][0])
    visited = [0] * (N + 1)
    result = 0
    for v in range(N+1):
        # 각 정점마다 dfs 실행 전에 visited 초기화
        visited[v] = 1
        dfs(v)
        visited[v] = 0
    print('#{} {}'.format(tc, result))