from collections import deque

import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
v = [-1] * 100001
q = deque()
q.append(N)
cnt = 0
v[N] = 0

while q:
    s = q.popleft()

    moves = [s-1, s+1, 2*s]

    if s == K:
        cnt += 1

    for move in moves:
        if 0 <= move <= 100000:
            if v[move] == -1 or v[move] >= v[s] + 1:
                q.append(move)
                v[move] = v[s] + 1

print(v[K])
print(cnt)
