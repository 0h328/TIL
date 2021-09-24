import sys
sys.stdin = open('input.txt')


def heap_push(value):
    global heap_count
    heap_count += 1  # 값을 하나 늘리고
    heap[heap_count] = value  # 그 자리에 값을 쓰고
    child = heap_count  # child -> index 번호
    parent = child // 2  # child의 부모 -> 자식 // 2

    # 루트 노드가 아니고(parent가 0인 경우는 root 노드 뿐) & 부모 노드 값 > 자식 노드 값 => swap (min_heap을 만들어야 하기 때문)
    while parent and heap[parent] > heap[child]:  # 부모가 0이 아니고(root가 아니고) / 부모 노드가 더 작을 때까지
        heap[parent], heap[child] = heap[child], heap[parent]  # 자식 <-> 부모 교환
        child = parent  # child를 기존 부모를 가리키는 key로 설정
        parent = child // 2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0] * (N+1)
    num = list(map(int, input().split()))
    heap_count = 0
    for i in range(len(num)):
        heap_push(num[i])
    i = N//2
    result = 0
    while i > 0:
        result += heap[i]
        i //= 2
    print('#{} {}'.format(tc, result))
