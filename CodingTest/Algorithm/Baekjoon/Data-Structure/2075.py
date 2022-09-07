import sys, heapq
sys.stdin = open('input.txt')

heap = []

for _ in range(int(sys.stdin.readline())):
    arr = list(map(int, sys.stdin.readline().split()))
    if not heap:
        for a in arr:
            heapq.heappush(heap, a)
    else:
        for a in arr:
            if heap[0] < a:
                heapq.heappush(heap, a)
                heapq.heappop(heap)

print(heap[0])