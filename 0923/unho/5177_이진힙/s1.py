import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    heap = [0]
    answer = 0

    for num in map(int, input().split()):
        heap.append(num)

        idx = len(heap)-1                                       # 맨뒤의 인덱스
        while heap[idx//2] > heap[idx]:                         # 부모노드의 값이 더 크면 자식과 교체
            heap[idx//2], heap[idx] = heap[idx], heap[idx//2]
            idx //= 2

    idx = len(heap)-1
    while idx > 0:
        answer += heap[idx//2]                                  # 부모 노드의 합 누적
        idx //= 2
    print('#{} {}'.format(tc, answer))
