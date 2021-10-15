import sys
sys.stdin=open('input.txt')

from heapq import heappush, heappop


def cost(x1, y1, x2, y2):  # 거리 및 요금 계산 함수
    return (abs(x1-x2)**2 + abs(y1-y2)**2) * E


def dijkstra(s):  # 다익스트라
    res = cnt = 0
    q = [(0, s)]  # 비용, 노드

    while q:
        d, a = heappop(q)
        if cnt == N: break
        if not vst[a]:
            vst[a] = True
            res += d
            cnt += 1
            for k, v in grp[a].items():
                if vst[k]: continue  # 방문한 곳 다시 방문 X
                heappush(q, (v, k))
    return res


ans = []
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X, Y = list(map(int, input().split())), list(map(int, input().split()))
    E = float(input())

    vst = [0] * N
    grp = [{} for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):  # 양방향이므로 양쪽 다 추가
            grp[i][j] = cost(X[i], Y[i], X[j], Y[j])
            grp[j][i] = cost(X[i], Y[i], X[j], Y[j])

    ans.append('#{0} {1:.0f}'.format(tc, dijkstra(0)))  # 소숫점 첫 번째 자리에서 반올림

print(*ans, sep='\n')