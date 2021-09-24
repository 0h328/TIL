import heapq
import sys
sys.stdin = open('input.txt')

# 부모 노드의 값 < 자식 노드의 값
# 마지막 노드의 조상 노드에 저장된 정수의 합 출력


"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    my_heap = list(map(int, input().split()))
    heapq.heapify(my_heap)
    ans = 0

    while N > 1:
        N //= 2
        ans += my_heap[N-1]

    print('#{} {}'.format(tc, ans))
"""