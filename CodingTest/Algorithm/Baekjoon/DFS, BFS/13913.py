from collections import deque
import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)

def locate(n, m):
    if n != m:
        locate(n, location[m])
    print(m, end=' ')

N, K = map(int, input().split())
v = [0] * 100001
q = deque()
q.append(N)
v[N] = 0
location = [0] * 100001

while q:
    s = q.popleft()

    moves = [s-1, s+1, s*2]

    if s == K:
        break

    for move in moves:
        if 0 <= move <= 100000 and v[move] == 0:
            q.append(move)
            v[move] = v[s] + 1
            location[move] = s

print(v[K])
locate(N, K)






