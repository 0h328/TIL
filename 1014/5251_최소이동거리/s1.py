import sys
from collections import deque
sys.stdin = open('input.txt')

def solve(v, cnt):
    global ans
    if v == N and visited[v] and cnt < ans:
        ans = cnt

    for w in stops[v]:
        if not visited[w[0]]:
            visited[w[0]] = 1
            solve(w[0], cnt + w[1])
            visited[w[0]] = 0

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    #N: 0~N번까지 정점
    #E: 도로 구간 개수
    temp = [list(map(int, input().split())) for _ in range(E)]
    # print(temp)
    stops = [[] for _ in range(N+1)]
    for idx in range(E):
        stops[temp[idx][0]].append((temp[idx][1], temp[idx][2]))
        #(idx번에서 갈 수 있는 정점, 거리)
    # print(stops)
    ans = 100
    visited = [0 for _ in range(N + 1)]
    ans_list = []
    for v in range(N+1):
        visited[v] = 1
        solve(v, 0)
        visited[v] = 0
        ans_list.append(ans)
    print(ans_list)
    print('#{} '.format(tc), end='')
    print(max(ans_list))