from collections import deque
import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

q = deque()
seq = []
for i in range(1, N+1):
    q.append(i)

print('<', end='')
while q:
    for i in range(K-1):
        a = q.popleft()
        q.append(a)
    print(q.popleft(), end='')
    if q:
        print(', ', end='')

print(">")