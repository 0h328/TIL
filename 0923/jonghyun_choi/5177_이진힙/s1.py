import sys
sys.stdin = open('input.txt')

import heapq

T = int(input())

for case in range(T):
    N = int(input())
    res = 0
    heap = list(map(int, input().split()))
    heapq.heapify(heap)
    heap = [0] + heap
    while N > 0:
        res += heap[N // 2]
        N //= 2

    print('#{} {}'.format(case + 1, res))

