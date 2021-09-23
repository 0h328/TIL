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


def heap_pop():
    global heap_count
    return_value = heap[1]
    heap[1] = heap[heap_count]
    heap[heap_count] = 0
    heap_count -= 1

    parent = 1
    child = parent * 2

    if child + 1 <= heap_count:
        if heap[child] > heap[child+1]:
            child += + 1

    while child <= heap_count and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2

        if child + 1 <= heap_count:
            if heap[child] > heap[child + 1]:
                child += + 1

    return return_value


heap_count = 0
nums = [7, 2, 5, 3, 4, 6]
N = len(nums)
heap = [0] * (N+1)

for i in range(N):
    heap_push(nums[i])
print(*heap)

for i in range(N):
    print(heap_pop(), end=' ')