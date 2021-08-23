def dfs(check1):
    stack = [check1]    # 시작 정점을 stack에 넣고 간다

    while stack:    # 모든 정점 방문 시까지
        check1 = stack.pop()
        if visited[check1] == 0:    # 방문 안한 경우의 조건
            visited[check1] = 1     # 안했을 경우 체크ㅓ

            for i in range(1, V + 1):  # 모든 정점에 대한 반복을 수행하며
                if G[check1][i] == 1 and not visited[i]:  # v의 인접 정점(w)이고 그곳이 아직 방문하지 않았다면
                    stack.append(i)
            if check1 == check2:
                return True

import sys
sys.stdin = open('input.txt')

T = int(input())
for num in range(T):

    # V(ertex), E(dge)
    V, E = map(int, input().split())
    tmp = []

    # 간선 정보 초기화
    for _ in range(E):
        t = list(map(int,input().split()))
        tmp.append(t)
    temp = [y for x in tmp for y in x]
    check1, check2 = map(int, input().split())

    # Graph 초기화
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        G[temp[i * 2]][temp[i * 2 + 1]] = 1
        G[temp[i * 2 + 1]][temp[i * 2]] = 1

    # 방문 표시 초기화
    visited = [0 for i in range(V+1)]
    # dfs 탐색 시작
    # if dfs(check1) == True:
    #     print("#{} {}".format(num+1, 1))
    # else:
    #     print("#{} {}".format(num + 1, 0))