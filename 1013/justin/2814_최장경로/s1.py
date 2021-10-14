def dfs(v, cnt):
    global ans
    visited[v] = 1                        # 방문 체크
    if cnt > ans:                         # (필요하면) 최댓값 갱신(최장 경로)
        ans = cnt

    for w in range(1, N+1):               # 정점 v의 인접 정점을 모두 확인하며
        if data[v][w] and not visited[w]: # 인접이며 방문 안한 경우
            dfs(w, cnt+1)                 # 인접인 경우 경로(cnt) 증가시키고 다시 그 정점(w)의 인접을 찾기 위해 재귀 호출
    visited[v] = 0                        # 다음 노드에서 출발하는 최장 경로를 찾기 위해 방문 체크 해제

                                          # for문 이후에 진행 (return 이후에 돌아오는 것은 for문 내부로 다시 돌아가는 것)
                                          # 다른 경로를 통해서 해당 정점에 오는 것은 허용 / 해당 정점에서 다른 경로로 나가는 것은 막기 위함
                                          # 핵심 -> 갈 수 있는 곳은 모두 가보고 & 방문 체크 풀어야 한다!

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())               # 정점의 수, 간선
    data = [[0] * (N+1) for _ in range(N+1)]       # 인접행렬
    visited = [0] * (N+1)                          # 방문 체크
    ans = 0

    for _ in range(M):                             # 무방향 그래프 설정
        A, B = map(int, input().split())
        data[A][B] = 1
        data[B][A] = 1

    for v in range(1, N+1):                      # 1번 노드부터 N번 노드에서 출발하는 모든 경우 체크
        dfs(v, 1)                                # 방문노드, 경로에 포함된 노드 개수

    print('#{} {}'.format(tc, ans))