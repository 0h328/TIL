import sys
sys.stdin = open('input.txt')


def dfs(idx, ans):
    global max_len
    visited[idx] = 1
    ans += 1        # 경로길이(= 지나간 노드 수) +1
    if ans > max_len:
        max_len = ans
    for num in node[idx]:
        if not visited[num]:    # 방문안한 노드 있으면
            dfs(num, ans)
    visited[idx] = 0    # 방문체크 초기화


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(M)]
    node = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    max_len = 0
    for x, y in info:   # 인접리스트로 간선정보 표현
        node[x].append(y)
        node[y].append(x)
    # print(node)
    # [[], [2], [1, 3], [2]]
    for i in range(N):
        dfs(i, 0)
    print('#{} {}'.format(tc, max_len))
