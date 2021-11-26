#큐
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

q = deque()
N = int(input())
for _ in range(N):
    com = input().split()

    if 'push' in com:
        q.append(com[1])
    elif 'pop' in com:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif 'size' in com:
        print(len(q))
    elif 'empty' in com:
        if q:
            print(0)
        else:
            print(1)
    elif 'front' in com:
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)