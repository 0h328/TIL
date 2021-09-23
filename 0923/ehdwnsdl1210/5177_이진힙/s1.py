import heapq
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)                     # 기존 리스트를 힙으로 변환

    # print(heap)

    heap = [0] + heap                       # 인덱스 탐색을 위해
    
    ancestor_sum = 0                        # 조상합!
    while N > 0:
        ancestor_sum += heap[N // 2]        # 조상은 // 2 이걸로 올라감! (마지막을 기준으로 하라고 함)
        N = N // 2

    print('#{} {}'.format(tc, ancestor_sum))