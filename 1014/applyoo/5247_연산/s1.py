import sys
sys.stdin=open('input.txt')


from collections import deque


def bfs(s):
    q = deque([(s, 0)])
    DP = [0] * (max(N, M)*2)

    while q:
        n, c = q.popleft()

        if n == M:
            return c

        for i in (n-1, n-10, n+1, n*2):
            if (0<i<len(DP)) and not DP[i]:
                DP[i] = c + 1
                q.append((i, c+1))


ans = []
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans.append('#{} {}'.format(tc, bfs(N)))
print(*ans, sep='\n')
