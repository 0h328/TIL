# 최소힙 - 직접 구현
"""
최소힙의 조건
1. 완전 이진 트리
2. 자식 < 부모
"""

#1.
def heap_push(value):               # heap push 연산
    global heap_count
    """
    핵심) 완전 이진 트리의 조건에 위배되지 않도록 연산 수행
    1. Tree의 가장 마지막에 요소 삽입
    2. 삽입된 노드와 부모 노드를 비교하여 swap
    3. 부모 노드보다 크거나/작고 and 루트 노드에 도달하기 전까지 반복
    """
    heap_count += 1                 # 값을 하나 늘리고
    heap[heap_count] = value        # 그 자리에 값을 쓰고
    child = heap_count              # child -> index 번호
    parent = child // 2             # child의 부모 -> 자식 // 2

    # 루트 노드가 아니고(parent가 0인 경우는 root 노드 뿐) & 부모 노드 값 > 자식 노드 값 => swap (min_heap을 만들어야 하기 때문)
    while parent and heap[parent] > heap[child]:              # 부모가 0이 아니고(root가 아니고) / 부모 노드가 더 작을 때까지
        heap[parent], heap[child] = heap[child], heap[parent] # 자식 <-> 부모 교환
        child = parent                                        # child를 기존 부모를 가리키는 key로 설정
        parent = child // 2                                   # parent는 기존 child를 가리키던 key로 교환

#2.
def heap_pop():
    global heap_count
    """
    핵심) 완전 이진 트리의 조건에 위배되지 않도록 연산 수행
    1. root 삭제 (최대힙이면 최댓값, 최소힙이면 최솟값이 반환)
     - heap에서는 루트의 원소만 삭제 가능
    2. Tree의 가장 마지막 요소를 root 자리로 이동 
    3. root 노드부터 시작해서 자식 노드 중 더 큰 값과 비교하며 swap 
    4. 조건을 만족하고 Tree의 가장 아래 도착할 때까지 반복
    """
    return_value = heap[1]      # root의 원소 백업하고 (return_value -> 하나의 for문에서 반환해야 하는 값)
    heap[1] = heap[heap_count]  # heap의 마지막 요소 값을 heap의 가장 위에 옮겨두고
    heap[heap_count] = 0        # heap의 마지막 요소는 0으로 변경(삭제)
    heap_count -= 1             # 마지막을 가리키는 위치 변경

    parent = 1
    child = parent * 2

    if child + 1 <= heap_count:          # 오른쪽 자식이 존재하고(heap_count는 마지막 요소를 가리키는 인덱스) + (완전 이진 트리이기 때문에 오른쪽 자식이 없다는 건 제일 마지막을 의미)
        if heap[child] > heap[child+1]:  # 왼쪽과 오른쪽 자식의 크기를 비교해서 왼쪽 자식이 더 크다면
            child = child + 1            # 오른쪽 자식과 교환할 수 있도록 child의 값을 오른쪽 자식의 인덱스에 맞춰준다. (아니라면 왼쪽을 그대로 유지)
                                         # (참고 - 더 작은 자식을 찾아 그 값과 바꾸는 이유는 큰 값과 변경하게되면 최소힙 조건을 유지할 수 없기 때문)

    while child <= heap_count and heap[parent] > heap[child]:   # 자식 노드가 하나라도 존재하고, 부모 노드가 > 자식 노드  -> swap
        heap[parent], heap[child] = heap[child], heap[parent]   # 부모 자식 노드 swap
        parent = child                                          # 기존 자식을 부모로
        child = parent * 2                                      # 자식을 부모로

        if child + 1 <= heap_count:           # 오른쪽 자식이 존재하고 (완전 이진 트리이기 때문에 오른쪽 자식이 없다는 건 제일 마지막을 의미)
            if heap[child] > heap[child+1]:   # 왼쪽과 오른쪽 자식의 크기를 비교해서 왼쪽 자식이 더 크다면
                child = child + 1             # 오른쪽 자식과 교환할 수 있도록 child의 값을 오른쪽 자식의 인덱스에 맞춰준다. (아니라면 왼쪽을 그대로 유지)
    return return_value

heap_count = 0
nums = [7, 2, 5, 3, 4, 6]
N = len(nums)
heap = [0] * (N+1)             # 크기 설정 (+1은 인덱스를 노드 번호에 맞추기 위해서 설정)

#1. heap push 연산
for i in range(N):
    heap_push(nums[i])         # 인덱스 0번에 해당하는 노드부터 heap_push 연산 수행
print(*heap)                   # 0 2 3 5 7 4 6

#2. heap pop 연산
for i in range(N):             # 삭제 - 루트 노드
    print(heap_pop(), end=' ') # 2 3 4 5 6 7