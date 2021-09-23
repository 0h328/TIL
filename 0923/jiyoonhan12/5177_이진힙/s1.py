import sys
sys.stdin = open('input.txt')


def heap_push(num):
    global heap_cnt
    heap_cnt += 1
    heap[heap_cnt] = num # 일단 n번째 자리에 넣고
    child = heap_cnt
    parent = heap_cnt // 2
    while parent and heap[parent] > heap[child]: # parent가 더 크면 자리 바꾸기
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


T = int(input())
for t in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))

    heap = [0] * (N+1)
    heap_cnt = 0

    for i in range(N): # 순서대로 최소힙에 저장
        heap_push(number[i])

    total = 0
    while N: # 조상 노드 합 구하기
        N //= 2
        total += heap[N]

    print('#{} {}'.format(t, total))