import sys
import heapq
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    heap = list(map(int, input().split()))

    heapq.heapify(heap)
    heap = [0] + heap
    # print(heap)

    answer = 0
    while N > 0:
        N = N // 2
        answer += heap[N]

    print('#{} {}'.format(tc, answer))
    ## heapify 쓰면 오답 나옴