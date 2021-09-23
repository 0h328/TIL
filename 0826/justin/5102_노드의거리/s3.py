def bfs(sv):
    Q = [sv]
    visited[sv] = 1
    distance = 0    # 거리 기록
    while Q:
        size = len(Q)           # Q의 길이는 유동적으로 변화 -> SIZE로 묶어서 컨트롤
        for _ in range(size):   # Q의 사이즈만큼 반복을 돌고
            v = Q.pop(0)
            if v == ev:
                return distance
            for w in range(1, V+1):
                if data[v][w] and not visited[w]:
                    Q.append(w)
                    visited[w] = 1
        distance += 1           # 반복 이후 거리 증가
    return 0

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        data[a][b] = data[b][a] = 1
    sv, ev = map(int, input().split())
    ans = bfs(sv)
    print('#{} {}'.format(tc, ans))

