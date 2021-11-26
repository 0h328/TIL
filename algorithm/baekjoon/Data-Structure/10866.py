import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

q = deque()
N = int(input())
for _ in range(N):
    com = input().split()

    if 'push_front' in com:
        q.appendleft(com[1])
    elif 'push_back' in com:
        q.append(com[1])
    elif 'pop_front' in com:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif 'pop_back' in com:
        if q:
            print(q.pop())
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
    elif 'back' in com:
        if q:
            print(q[-1])
        else:
            print(-1)

