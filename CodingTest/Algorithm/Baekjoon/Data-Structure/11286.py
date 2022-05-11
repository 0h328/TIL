import sys, heapq
sys.stdin = open('input.txt')

N = int(input())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:              # x가 0일때
        if not heap:        # 배열이 비어있는 경우엔
            print(0)        # 0을 출력
        else:               # 힙에 값이 있다면
            print(heapq.heappop(heap)[1])   # 튜플로 묶어준 절댓값이 가장 작은 값(정수 값-idx[1]) 출력+제거
    else:                   # x가 정수이면
        heapq.heappush(heap, (abs(x), x))   # heap에 절댓값x와 정수x를 튜플로 묶어서 넣기(포인트!!!)
