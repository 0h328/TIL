import sys, heapq
sys.stdin = open('input.txt')

N = int(input())
heap = []
for i in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])   # 0번째 idx로 최소 힙을 구성했으므로, 1번째 idx로 최대 힙을 출력
    else:
        heapq.heappush(heap, (-x, x))   # 튜플로 구성하면 맨 앞의 값을 기준으로 최소 힙이 구성됨
