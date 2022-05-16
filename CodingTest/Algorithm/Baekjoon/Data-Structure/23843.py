import sys
import heapq
sys.stdin = open('input.txt')

N, M = map(int, input().split())
equip = list(map(int, input().split()))
equip.sort(reverse=True)
heap = []

for e in equip:
    if len(heap) < M:
        heapq.heappush(heap, e)
    else:
        tmp = heapq.heappop(heap)
        heapq.heappush(heap, tmp + e)

print(max(heap))

# 1. 시간이 오래 걸리는 전자 기기부터 충전시키는 방식으로 진행
# 2. 시간을 계산하기 위해서는 최소 히프를 사용해 준다.
# 2-1. 히프에 현재 충전중인 전자 기기가 걸리는 시간을 넣어 준다.
# 2-2. 히프가 가득 차지 않은 경우에는 충전기 자리가 남아있는 것이므로 전자기기의 충전 시간을 그대로 넣어준다.
# 2-3. 히프가 가득 찬 경우는 충전기가 꽉 찬 경우이므로 기기를 하나 빼준 다음에 넣어주어야 한다. 따라서 히프에서요소 하나를 빼준 후, 해당 요소의 값에 현재 전자기기의 충전 시간을 더해서 다시 히프에 넣어준다.
# 3. 히프 내의 최댓값을 구해서 출력시켜 준다.
# 3-1. 히프 내의 최댓값이 의미하는 것은 마지막으로 충전이 완료되는 시간이다.