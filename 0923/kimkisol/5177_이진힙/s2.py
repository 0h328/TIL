import sys
import heapq

sys.stdin = open('input.txt')


# 이건 왜 테스트케이스 3개가 틀리게 나오는지 모르겠음 (heap 리스트 앞에 [0] 붙여주면 됨)
T = int(input())

for t in range(1, T + 1):
    N = int(input())

    nums = list(map(int, input().split())) # heapq 라이브러리 사용시 0 없애줘야 함
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

    # heap 리스트 앞에 [0] 붙여줘야 됨
    result = 0

    while N:  # 가장 마지막 노드 번호
        N = (N - 1) // 2  # 0이 없기 때문에 -1하고 //2한 값이 부모의 노드 번호가 됨
        result += heap[N]

    print('#{} {}'.format(t, result))
