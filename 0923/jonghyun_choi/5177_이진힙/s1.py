import sys
sys.stdin = open('input.txt')

import heapq

T = int(input())

for case in range(T):
    N = int(input())
    res = 0
    tree = list(map(int, input().split()))
    heap = []
    for i in tree:
        heapq.heappush(heap, i)
    heap = [0] + heap
    while N > 1:
        N //= 2
        res += heap[N]

    print('#{} {}'.format(case + 1, res))

