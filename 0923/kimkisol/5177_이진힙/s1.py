import sys

sys.stdin = open('input.txt')


# [숫자 하나씩 들어올 때마다 heap 규칙에 맞게 push]
def heap_push(value):
    global heap_count

    heap_count += 1
    heap[heap_count] = value
    child = heap_count
    parent = child // 2

    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    heap = [0] * (N + 1)
    heap_count = 0
    result = 0

    for i in range(N):
        heap_push(nums[i])

    while N:  # 가장 마지막 노드 번호
        N //= 2  # 해당 노드의 부모
        result += heap[N]

    print('#{} {}'.format(t, result))


# [트리 전체가 있는 상태에서 정렬]
# T = int(input())
#
# for t in range(1, T + 1):
#     N = int(input())
#     heap = [0] + list(map(int, input().split()))
#     result = 0
#
#     for i in range(1, N):
#         parent = i
#         child = parent * 2
#         if child <= N:  # 왼쪽 자식이 범위 내일 경우
#             if child + 1 <= N:  # 오른쪽 자식이 범위 내일 경우
#                 child = child if heap[child] < heap[child + 1] else child + 1  # 더 작은 쪽을 child 번호로 저장
#
#             while child <= N and heap[parent] > heap[child]:  # child가 범위 내이며, 부모가 자식보다 큰 경우 (작은 경우는 swap 필요 없음)
#                 heap[parent], heap[child] = heap[child], heap[parent]  # 부모, 자식 swap
#                 parent = child  # swap돼서 현재 노드값은 자식 노드 번호에 저장되어 있음
#                 child = parent * 2  # 왼쪽 자식 우선 저장
#                 if child + 1 <= N:  # 오른쪽 자식이 있을 경우
#                     child = child if heap[child] < heap[child + 1] else child + 1  # 더 작은 쪽을 child 번호로 저장
#
#     print(heap)
#     while N:  # 가장 마지막 노드 번호
#         N //= 2  # 해당 노드의 부모
#         result += heap[N]
#
#     print('#{} {}'.format(t, result))
