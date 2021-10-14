import sys
sys.stdin = open('input.txt')

def dfs(i, cnt):
    global result

    if cnt > result:
        return

    if i == N:
        if result > cnt:
            result = cnt
        return
    for v in N_list[i]:     # N_list[i]랑 연결된 것들 돌기
        if not visited[v[0]]:  # v를 방문하지 않았으면
            visited[v[0]] = 1  # 방문 표시
            dfs(v[0], cnt + v[1]) # cnt 1 늘리고 v로 dfs
            visited[v[0]] = 0  # 방문 해제

tc = int(input())
for t in range(1, tc + 1):
    result = 1e9
    N, E = map(int, input().split())
    N_list = [[] for _ in range (N)]
    for i in range(E):  # 인접 리스트
        s, e, w = map(int, input().split())
        N_list[s].append((e, w))
    visited = [0] * (N + 1) # 방문 여부
    dfs(0, 0)
    print("#{} {}".format(t, result))