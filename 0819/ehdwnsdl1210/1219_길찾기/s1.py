# 유향(방향이 있음)
    # 어떻게 가져옴?
    # 1) 홀 / 짝
    # 2) 2step for i in range(0, len(raod), 2)
    # 3) 2 * i / 2 * i + 1

    # 어떻게 저장함?
    # ch1, ch2 = [0] * 100 / ch1에 있다면, ch2에 넣어라

from pandas import DataFrame
import sys
sys.stdin = open('input.txt')

# for _ in range(10):
#     tc, N = map(int, input().split())
#     road = list(map(int, input().split()))
#
#     # 3)
#     # for i in range(N):
#     #     st = road[2*i]
#     #     ed = road[2*i+1]
#
#     # 저장
#     ch1 = [0] * 100
#     ch2 = [0] * 200
#
#     for i in range(N):
#         if ch1[road[2*i]] == 0:
#             ch1[road[2*i]] = road[2*i+1]
#         else:
#             ch2[road[2*i]] = road[2*i+1]
#
#     # 인접행렬
#     adj_arr = [[0] * 100 for _ in range(100)]
#     for i in range(N):
#         adj_arr[road[2*i]][road[2*i+1]] = 1
#         # adj_arr[road[2*i+1]][road[2*i]] = 1   # 유향(양방향)일 경우 추가
#
#     # 인접리스트
#     adj_list = [[] for _ in range(100)]
#     for i in range(N):
#         adj_list[road[2*i]].append([road[2*i+1]])
#
#     visited = [0] * 100
#     ans = 0
#
#     stack = [0]
#
#     while stack:
#         curr = stack.pop()
#
#         if curr == 99:
#             ans = 1
#             break
#         # 방문 안했으면
#
#         # 방문 했으면 건너가~
#         if visited[curr]: continue
#         visited[curr] = 1
#
#         for w in adj_list[curr]:
#             if not visited[w]:
#                 stack.append(w)
#
#     print('#{} {}'.format(tc, ans))

def DFS(v):
    global ans
    if v == 99:
        ans = 1
        return

    visited[v] = 1

    for w in range(100):
        if not visited[w] and adj_arr[v][w]:
            DFS(w)  # return 안함 : 다른 경우를 안한다. (모든 분기를 해야...)

for _ in range(10):
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))

    adj_arr = [[0] * 100 for _ in range(100)]
    for i in range(N):
        adj_arr[road[2 * i]][road[2 * i + 1]] = 1

    visited = [0] * 100
    ans = 0

    DFS(0)
    print('#{} {}'.format(tc, ans))

"""
def dfs(v):
    if not visited[v]:
        visited[v] = 1
    for w in range(1, N+1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)


for _ in range(10):
    T, N = map(int, input().split())    # N은 E(간선 수)
    L = list(map(int, input().split())) # 간선 정보 초기화 temp
    G = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(N):
        G[L[i]][L[i+1]] = 1
        G[L[i+1]][L[i]] = 1
    # print(DataFrame(G))

    visited = [0 for _ in range(N+1)]

    print(dfs(0))  # 0번 정점부터 탐색 시작
"""