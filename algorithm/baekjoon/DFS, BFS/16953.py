import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

A, B = map(int, input().split())
q = deque()
q.append((A, 1))

while q:
    s, cnt = q.popleft()

    if s*2 <= B:
        q.append((s*2, cnt+1))
    if s*10+1 <= B:
        q.append((s*10+1, cnt+1))
    if s == B:
        print(cnt)
        exit()

print(-1)



