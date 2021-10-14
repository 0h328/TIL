import sys
sys.stdin=open('input.txt')


from heapq import heappush, heappop


def bfs(s):
    q = [(0, s)]
    res = cnt = 0

    while q:
        w, n = heappop(q)

        if cnt == (N+1): return res

        if not vst[n]:
            vst[n] = 1
            res += w
            cnt += 1
            for k, v in A[n].items():
                heappush(q, (v, k))


ans = []
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    A = [{} for _ in range(N+1)]
    for _ in range(M):
        n1, n2, w = map(int, input().split())
        if n1 in A[n2]:
            A[n1][n2] = min(A[n1][n2], w)
            A[n2][n1] = min(A[n2][n1], w)
        else:
            A[n1][n2] = w
            A[n2][n1] = w

    vst = [0] * (N+1)
    ans.append('#{} {}'.format(tc, bfs(1)))
print(*ans, sep='\n')
