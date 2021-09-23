import sys
sys.stdin = open('input.txt')

T = int(input())

def make_heap(data):
    global heap_count

    heap_count += 1
    heap[heap_count] = data
    child = heap_count
    parent = child // 2

    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2

def cnt_sum(node):
    cnt = 0

    while node:
        node = node // 2
        cnt += heap[node]

    return cnt

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    heap = [0] * (N + 1)
    heap_count = 0

    for num in data:
        make_heap(num)

    ans = cnt_sum(N)

    print('#{} {}'.format(tc, ans))