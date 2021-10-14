import sys
sys.stdin = open('input.txt')

def dfs(i, cnt):
    global result

    if result < cnt:
        result = cnt
    for v in N_list[i]:     # N_list[i]랑 연결된 것들 돌기
        if not visited[v]:  # v를 방문하지 않았으면
            visited[v] = 1  # 방문 표시
            dfs(v, cnt + 1) # cnt 1 늘리고 v로 dfs
            visited[v] = 0  # 방문 해제

tc = int(input())
for t in range(1, tc + 1):
    result = 0
    N, M = map(int, input().split())
    N_list = [[] * (N + 1) for _ in range(N + 1)]
    for i in range(M):  # 인접 리스트
        x, y = map(int, input().split())
        N_list[x].append(y)
        N_list[y].append(x)
    visited = [0] * (N + 1) # 방문 여부
    for i in range(1, N + 1):
        visited[i] = 1  # 현재 i 방문 체크
        dfs(i, 1)       # dfs
        visited[i] = 0  # 다음 반복을 위해 visited 초기화
    print("#{} {}".format(t, result))