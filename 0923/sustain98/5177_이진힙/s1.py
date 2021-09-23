import sys
sys.stdin = open('input.txt')
import heapq

t = int(input())
for idx in range(1, t+1):
    n = int(input())
    tree = list(map(int, input().split()))
    heap = []
    for i in tree:
        heapq.heappush(heap, i)
    heap = [0] + heap
    res = 0
    while n > 1:
        n //= 2
        res += heap[n]
    print('#{} {}'.format(idx, res))
