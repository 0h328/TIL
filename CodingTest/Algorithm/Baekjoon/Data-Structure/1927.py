import sys, heapq
sys.stdin = open('input.txt')

N = int(input())
heap = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:                          # x가 0이면
        if not heap:                    # 빈 배열이면
            print(0)                    # 0을 출력
        else:                           # 배열에 수가 있으면
            print(heapq.heappop(heap))  # 배열의 가장 작은 값 출력
    else:                       # x가 자연수면
        heapq.heappush(heap, x) # 배열에 값을 넣음
