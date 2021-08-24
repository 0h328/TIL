# dfs
# S에서 G로가는 경로가 있으면 '1', 없으면 '0'

from pandas import DataFrame
import sys
sys.stdin = open('input.txt')

'''
T = int(input())

def dfs(s, g):
    for i in B[s]:
        for j in range(len(B)):
            if i == 1 and B[j][g] == 1:
                return 1

for tc in range(1, T+1):
    V, E = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    B = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(len(P)):
        B[P[i][0]][P[i][1]] = 1 # 유향(단방향)

    # print(DataFrame(B))
    print('#{} {}'.format(tc, dfs(S, G)))
'''

def DFS(start, goal):
    stack = [start] # stack에 탐색을 시작 할 노드를 넣어놓자!

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1

            for w in G[v]:
                # if visited[w]:
                #     continue
                stack.append(w)

    return visited[goal]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for _ in range(E):
        s, e = map(int, input().split())
        G[s].append(e)

    start, goal = map(int, input().split())

    ans = DFS(start, goal)
    print('#{} {}'.format(tc, ans))

# Ctrl + Alt + Shift + j : 같은거 다 바꾸기