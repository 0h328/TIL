import sys
from collections import deque
sys.stdin = open('input.txt')


def in_order(node):
    if node*2 <= N:
        in_order(node*2)

    heap[node] = q.popleft()

    if node*2 + 1 <= N:
        in_order(node*2 + 1)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    q = deque(list(range(1, N+1)))

    heap = [0] * (N+1)

    in_order(1)

    print('#{} {} {}'.format(tc, heap[1], heap[N//2]))