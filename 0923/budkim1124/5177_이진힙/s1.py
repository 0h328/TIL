import sys
sys.stdin = open('input.txt')


def heap_push(value):
    global heap_count

    heap_count += 1
    h_list[heap_count] = value
    child = heap_count
    parent = child // 2

    while parent and h_list[parent] > h_list[child]:
        h_list[parent], h_list[child] = h_list[child], h_list[parent]
        child = parent
        parent = child // 2

def heap_pop():
    global heap_count
    return_value = h_list[1]
    h_list[1] = h_list[heap_count]
    h_list[heap_count] = 0
    heap_count -= 1

    parent = 1
    child = parent * 2

    if child + 1 <= heap_count:
        if h_list[child] > h_list[child+1]:
            child = child + 1


    while child <= heap_count and h_list[parent] > h_list[child]:
        h_list[parent], h_list[child] = h_list[child], h_list[parent]
        parent = child
        child = parent * 2

        if child + 1 <= heap_count:
            if h_list[child] > h_list[child+1]:
                child = child + 1
    return return_value


T = int(input())

for t in range(T):
    heap_count = 0
    h_list = list(map(int, input().split()))
    N = len(h_list)
    heap = [0] * (N+1)

    for i in range(0,N+1):
        heap_push(h_list[i])

    for i in range(0,N+1):
        print(heap_pop(), end=' ')



